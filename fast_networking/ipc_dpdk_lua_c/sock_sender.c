/*
 * this program read from shared memory and then write send it to remote host
 * via TCP socket
 */
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


static volatile int keepRunning = 1;
void intHandler(int dummy) {
	keepRunning = 0;
	printf("catch ctrl-c\n");
	if (shm_unlink(SHM_NAME) != 0) {
		perror("shmunlink failed");
	}

	if (sem_unlink(SEM_RING) != 0) {
		perror("sem_unlink failed");
	}
	if (sem_unlink(SEM_MUTEX_RING) != 0) {
		perror("sem_unlink failed");
	}
	exit(1);
}

int main(int argc, char *argv[]) {
	int sock;
	struct sockaddr_in server;

	struct shm_data_t *shm_data;
	int shm_size = sizeof(struct shm_data_t);

	signal(SIGINT, intHandler);

	// check input
	if (argc != 2) {
		perror("usage : sock_sender remote_host");
		exit(1);
	}

	// create socket
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		perror("can't create socket");
		exit(1);
	}

	server.sin_addr.s_addr = inet_addr(argv[1]);
	server.sin_family = AF_INET;
	server.sin_port = htons(8000);

	// connect to receiver
	if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0) {
		perror("connect failed");
		exit(1);
	}


	printf("connected to remote addr\n");

	// init IPC
	// -- create semaphore
	sem_t *sem_ring =sem_open(SEM_RING, O_CREAT, S_IRUSR | S_IWUSR, 0);
	sem_t *sem_mutex = sem_open(SEM_MUTEX_RING, O_CREAT, S_IRUSR | S_IWUSR, 1);

	// -- create shared mem
	int shm_fd = shm_open(SHM_NAME,  O_CREAT | O_RDWR, S_IRWXU | S_IRWXG);
	if (shm_fd < 0) {
		perror("failed to create shared mem");
		exit(1);
	}

	ftruncate(shm_fd, sizeof(struct shm_data_t));

	// -- mmap
	shm_data = (struct shm_data_t *)mmap(NULL, shm_size, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (shm_data == NULL) {
		perror("mmap failed");
		exit(1);
	}
	shm_data->capacity = RING_LEN;
	shm_data->length = 0;

	// loop forever,waiting for data
	while(keepRunning) {
		sem_wait(sem_ring);

		sem_wait(sem_mutex);
		// use the data
		//printf("use data index = %d\n", shm_data->start);
		if( send(sock , shm_data->data[shm_data->start] , 1024 , 0) < 0) {
			printf("Send failed\n");
			fflush(stdout);
		}
		shm_data->start = (shm_data->start + 1) % RING_LEN;
		shm_data->length = shm_data->length -1;

		sem_post(sem_mutex);
	}
}
