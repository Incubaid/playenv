#define NETMAP_WITH_LIBS
#include <net/netmap_user.h>
#include <poll.h>
#include <stdio.h>
#include <string.h>
#include <netinet/ether.h>
#include <arpa/inet.h>

void use_data(unsigned char *buf, uint32_t len);


void receiver(void)
{
	struct	nm_desc	*d;
	struct	pollfd fds;
	u_char	*buf;
	struct	nm_pkthdr h;
	
	//...
	d = nm_open("netmap:eth1", NULL, 0, 0);
	fds.fd	= NETMAP_FD(d);
	fds.events = POLLIN;
	for (;;) {
		poll(&fds,	1, -1);
		while ( (buf = nm_nextpkt(d, &h)) )
			use_data(buf, h.len);
	}
	nm_close(d);
}



void use_data(unsigned char *buf, uint32_t len) {
	unsigned char data[1500];
	int data_len;
	struct ether_header *eh = (struct ether_header *) buf;
	if (ntohs(eh->ether_type) == 0x8915 && len > 15) {
		data_len = buf[14];
		memcpy(data, buf + 15 , data_len);
		printf("data = %s\n", data);
		fflush(stdout);
	}
}
int main() {
	receiver();
}

/*
void receiver(void) {
	struct netmap_if *nifp;
	struct nmreq req;
	int i, len;
	char *buf;

	int fd = open("/dev/netmap", 0);
	strcpy(req.nr_name, "ix0"); // register the interface
	ioctl(fd, NIOCREGIF, &req); // offset of the structure
	void *mem = mmap(NULL, req.nr_memsize, PROT_READ|PROT_WRITE, 0, fd, 0);
	nifp = NETMAP_IF(mem, req.nr_offset);
	for (;;) {
		struct pollfd x[1];
		struct netmap_ring *ring = NETMAP_RXRING(nifp, 0);
		
		x[0].fd = fd;
		x[0].events = POLLIN;
		poll(x, 1, 1000);
		for ( ; ring->avail > 0 ; ring->avail--) {
			i = ring->cur;
			buf = NETMAP_BUF(ring, i);
			use_data(buf, ring->slot[i].len);
			ring->cur = NETMAP_NEXT(ring, i);
		}
	}
}
*/

