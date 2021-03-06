/*-
 *   BSD LICENSE
 *
 *   Copyright(c) 2010-2015 Intel Corporation. All rights reserved.
 *   All rights reserved.
 *
 *   Redistribution and use in source and binary forms, with or without
 *   modification, are permitted provided that the following conditions
 *   are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in
 *       the documentation and/or other materials provided with the
 *       distribution.
 *     * Neither the name of Intel Corporation nor the names of its
 *       contributors may be used to endorse or promote products derived
 *       from this software without specific prior written permission.
 *
 *   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 *   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 *   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 *   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 *   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdint.h>
#include <inttypes.h>
#include <rte_eal.h>
#include <rte_ethdev.h>
#include <rte_cycles.h>
#include <rte_lcore.h>
#include <rte_mbuf.h>
#include <arpa/inet.h>

#include <semaphore.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define RX_RING_SIZE 128
#define TX_RING_SIZE 512

#define NUM_MBUFS 8191
#define MBUF_CACHE_SIZE 250
#define BURST_SIZE 32

static const struct rte_eth_conf port_conf_default = {
	.rxmode = { .max_rx_pkt_len = ETHER_MAX_LEN }
};

#define DEST_MAC0	0x08
#define DEST_MAC1	0x00
#define DEST_MAC2	0x27
#define DEST_MAC3	0xaf
#define DEST_MAC4	0xbc
#define DEST_MAC5	0x9b

#define RING_LEN 10

struct shm_data_t {
	char data[RING_LEN][1024];
	int capacity;
	int length;
	int start; // read index
	int end_idx; // write index
};

#define SHM_NAME "myshm"
#define SEM_RING "sem_ring"
#define SEM_MUTEX_RING "sem_mutex"

static struct shm_data_t *shm_data;
static sem_t *sem_ring;
static sem_t *sem_mutex;
static int shm_fd;

static void init_ipc(void) {
	// -- create semaphore
	sem_ring =sem_open(SEM_RING, O_CREAT, S_IRUSR | S_IWUSR, 0);
	sem_mutex = sem_open(SEM_MUTEX_RING, O_CREAT, S_IRUSR | S_IWUSR, 1);

	// -- create shared mem
	shm_fd = shm_open(SHM_NAME,  O_CREAT | O_RDWR, S_IRWXU | S_IRWXG);
	if (shm_fd < 0) {
		perror("failed to create shared mem");
		exit(1);
	}

	if (ftruncate(shm_fd, sizeof(struct shm_data_t)) < 0) {
		perror("ftruncate failed");
		exit(1);
	}

	// -- mmap
	shm_data = (struct shm_data_t *)mmap(NULL, sizeof(struct shm_data_t), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (shm_data == NULL) {
		perror("mmap failed");
		exit(1);
	}
	shm_data->capacity = RING_LEN;
	shm_data->length = 0;

}

static void deinit_ipc(void) {
	if (shm_unlink(SHM_NAME) != 0) {
		perror("shmunlink failed");
	}

	if (sem_unlink(SEM_RING) != 0) {
		perror("sem_unlink failed");
	}
	if (sem_unlink(SEM_MUTEX_RING) != 0) {
		perror("sem_unlink failed");
	}

}



/*
 * Initializes a given port using global settings and with the RX buffers
 * coming from the mbuf_pool passed as a parameter.
 */
static inline int
port_init(uint8_t port, struct rte_mempool *mbuf_pool)
{
	struct rte_eth_conf port_conf = port_conf_default;
	const uint16_t rx_rings = 1, tx_rings = 1;
	int retval;
	uint16_t q;

	if (port >= rte_eth_dev_count())
		return -1;

	/* Configure the Ethernet device. */
	retval = rte_eth_dev_configure(port, rx_rings, tx_rings, &port_conf);
	if (retval != 0)
		return retval;

	/* Allocate and set up 1 RX queue per Ethernet port. */
	for (q = 0; q < rx_rings; q++) {
		retval = rte_eth_rx_queue_setup(port, q, RX_RING_SIZE,
				rte_eth_dev_socket_id(port), NULL, mbuf_pool);
		if (retval < 0)
			return retval;
	}

	/* Allocate and set up 1 TX queue per Ethernet port. */
	for (q = 0; q < tx_rings; q++) {
		retval = rte_eth_tx_queue_setup(port, q, TX_RING_SIZE,
				rte_eth_dev_socket_id(port), NULL);
		if (retval < 0)
			return retval;
	}

	/* Start the Ethernet port. */
	retval = rte_eth_dev_start(port);
	if (retval < 0)
		return retval;

	/* Display the port MAC address. */
	struct ether_addr addr;
	rte_eth_macaddr_get(port, &addr);
	printf("Port %u MAC: %02" PRIx8 " %02" PRIx8 " %02" PRIx8
			   " %02" PRIx8 " %02" PRIx8 " %02" PRIx8 "\n",
			(unsigned)port,
			addr.addr_bytes[0], addr.addr_bytes[1],
			addr.addr_bytes[2], addr.addr_bytes[3],
			addr.addr_bytes[4], addr.addr_bytes[5]);

	/* Enable RX in promiscuous mode for the Ethernet device. */
	rte_eth_promiscuous_enable(port);

	return 0;
}

static uint16_t send_data(struct rte_mempool *mbuf_pool, uint8_t port_id, const char *data, size_t data_len) 
{

	struct rte_mbuf *pkt = rte_pktmbuf_alloc(mbuf_pool);

	int pkt_size = sizeof(struct ether_hdr) + data_len;
	pkt->data_len = pkt_size;
	pkt->pkt_len = pkt_size;
	struct ether_hdr *eth_hdr = rte_pktmbuf_mtod(pkt, struct ether_hdr *);
	
	rte_eth_macaddr_get(0, &eth_hdr->s_addr);
		
	
	eth_hdr->d_addr.addr_bytes[0] = DEST_MAC0;
	eth_hdr->d_addr.addr_bytes[1] = DEST_MAC1;
	eth_hdr->d_addr.addr_bytes[2] = DEST_MAC2;
	eth_hdr->d_addr.addr_bytes[3] = DEST_MAC3;
	eth_hdr->d_addr.addr_bytes[4] = DEST_MAC4;
	eth_hdr->d_addr.addr_bytes[5] = DEST_MAC5;
	eth_hdr->ether_type = htons(0x8915);
		
	
	char *data_ptr = rte_ctrlmbuf_data(pkt);
	rte_memcpy(data_ptr+sizeof(struct ether_hdr), data, data_len);
	
	struct rte_mbuf *bufs[1];
	bufs[0] = pkt;
	
	return rte_eth_tx_burst(port_id, 0, bufs, 1);
}

/*
 * The lcore main. This is the main thread that does the work, reading from
 * an input port and writing to an output port.
 */
static __attribute__((noreturn)) void
lcore_main(struct rte_mempool *mbuf_pool)
{
	const uint8_t nb_ports = rte_eth_dev_count();
	uint8_t port;

	/*
	 * Check that the port is on the same NUMA node as the polling thread
	 * for best performance.
	 */
	for (port = 0; port < nb_ports; port++)
		if (rte_eth_dev_socket_id(port) > 0 &&
				rte_eth_dev_socket_id(port) !=
						(int)rte_socket_id())
			printf("WARNING, port %u is on remote NUMA node to "
					"polling thread.\n\tPerformance will "
					"not be optimal.\n", port);

	printf("\nCore %u sending packets. [Ctrl+C to quit]\n",
			rte_lcore_id());

	/* Run until the application is quit or killed. */
	for (;;) {
		sem_wait(sem_ring);
		sem_wait(sem_mutex);
		
		send_data(mbuf_pool, 0, shm_data->data[shm_data->start], 1024);
		shm_data->start = (shm_data->start + 1) % RING_LEN;
		shm_data->length = shm_data->length -1;
		
		sem_post(sem_mutex);
	}
	printf("finished to send data\n");
}

/*
 * The main function, which does initialization and calls the per-lcore
 * functions.
 */
int
main(int argc, char *argv[])
{
	struct rte_mempool *mbuf_pool;
	unsigned nb_ports;
	uint8_t portid;

	deinit_ipc();
	init_ipc();

	/* Initialize the Environment Abstraction Layer (EAL). */
	int ret = rte_eal_init(argc, argv);
	if (ret < 0)
		rte_exit(EXIT_FAILURE, "Error with EAL initialization\n");

	argc -= ret;
	argv += ret;

	/* Check that there is an even number of ports to send/receive on. */
	nb_ports = rte_eth_dev_count();
	
	printf("nb_ports = %d\n", nb_ports);
	/* Creates a new mempool in memory to hold the mbufs. */
	mbuf_pool = rte_pktmbuf_pool_create("MBUF_POOL", NUM_MBUFS * nb_ports,
		MBUF_CACHE_SIZE, 0, RTE_MBUF_DEFAULT_BUF_SIZE, rte_socket_id());

	if (mbuf_pool == NULL)
		rte_exit(EXIT_FAILURE, "Cannot create mbuf pool\n");

	/* Initialize all ports. */
	for (portid = 0; portid < nb_ports; portid++)
		if (port_init(portid, mbuf_pool) != 0)
			rte_exit(EXIT_FAILURE, "Cannot init port %"PRIu8 "\n",
					portid);

	if (rte_lcore_count() > 1)
		printf("\nWARNING: Too many lcores enabled. Only 1 used.\n");

	/* Call lcore_main on the master core only. */
	lcore_main(mbuf_pool);

	return 0;
}
