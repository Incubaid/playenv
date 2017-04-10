#include <sys/mman.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <semaphore.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <errno.h>


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

void init_ipc() {
	// -- create semaphore
	sem_ring =sem_open(SEM_RING, O_CREAT, S_IRUSR | S_IWUSR, 0);
	sem_mutex = sem_open(SEM_MUTEX_RING, O_CREAT, S_IRUSR | S_IWUSR, 1);

	// -- create shared mem
	shm_fd = shm_open(SHM_NAME,  O_CREAT | O_RDWR, S_IRWXU | S_IRWXG);
	if (shm_fd < 0) {
		perror("failed to create shared mem");
		exit(1);
	}

	ftruncate(shm_fd, sizeof(struct shm_data_t));

	// -- mmap
	shm_data = (struct shm_data_t *)mmap(NULL, sizeof(struct shm_data_t), PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (shm_data == NULL) {
		perror("mmap failed");
		exit(1);
	}
	shm_data->capacity = RING_LEN;
	shm_data->length = 0;

}

void deinit_ipc() {
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


static volatile int keepRunning = 1;
void intHandler(int dummy) {
	keepRunning = 0;
	deinit_ipc();
	exit(1);
}

int main() {
	int sock, client_sock, c;
	struct sockaddr_in server, client;
	
	signal(SIGINT, intHandler);

	// create socket
	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock < 0) {
		perror("failed to create socket");
		exit(1);
	}

	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(8000);

	// set reuse port
	if (setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &(int){ 1 }, sizeof(int)) < 0) {
		perror("setsockopt(SO_REUSEADDR) failed");
		exit(1);
	}

	// bind
	if( bind(sock,(struct sockaddr *)&server , sizeof(server)) < 0) {
		perror("bind failed");
		exit(1);
	}

	init_ipc();

	c = sizeof(struct sockaddr_in);
	listen(sock, 3);

	// accpet
	client_sock = accept(sock, (struct sockaddr *)&client, (socklen_t*)&c);
	printf("got a client");
	fflush(stdout);

	char msg[1024];
	int recv_size;
	int i = 0;

	// receive until the end
	while(keepRunning) {
		recv_size = recv(client_sock, msg, 1024, 0);
		if (recv_size <= 0) {
			perror("disconnected");
			break;
		}
		
		sem_wait(sem_mutex);
		memcpy(shm_data->data[shm_data->start], msg, 1024);
		shm_data->start = (shm_data->start + 1) % shm_data->capacity;
		sem_post(sem_mutex);
		sem_post(sem_ring);

		printf("i = %d\n", i++);
		if(i % 100 == 0) {
			fflush(stdout);
		}
	}
}
