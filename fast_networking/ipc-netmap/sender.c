#define NETMAP_WITH_LIBS
#include <net/netmap_user.h>
#include <poll.h>
#include <stdio.h>
#include <string.h>
#include <netinet/ether.h>
#include <arpa/inet.h>
#include <sys/time.h>

#include "test.h"

void sender(void)
{
	struct	nm_desc	*d;
	char data[1024];
	struct pollfd pfd;

	memset(data, 'a', 1024);
	
	/**
	 * Opening netmap device as master.
	 * It is actually very simple to open it slave, simply using below line
	 *			d = nm_open("netmap:eth1{0", NULL, 0, 0);
	 *
	 * but we want to show how to change tx_slots & rx_slots value below
	 */

	struct nmreq req;
	bzero(&req, sizeof(req));
	req.nr_tx_slots = TX_SLOTS;
	req.nr_rx_slots = RX_SLOTS;
	req.nr_arg1 = 0;
	req.nr_arg2 = 1;
	req.nr_flags = NR_REG_PIPE_MASTER;
	
	d = nm_open("netmap:eth1", &req, 0, 0);
	if (d == NULL) {
		perror("failed to open");
		exit(1);
	}
	print_nmreq(d->req);

	pfd.fd = d->fd;
	pfd.events = POLLOUT;
	
	int sent = 0;

	struct timeval t1, t2;
	gettimeofday(&t1, NULL);
	for (sent = 0; sent < TO_SEND; sent++) {
		if (nm_inject(d, (const void *)data, 1024) <= 0) {
			fprintf(stderr, "polling after %d sent\n", sent);
			sent--;
			poll(&pfd, 1, 1000);
			continue;
		}
	}
	gettimeofday(&t2, NULL);

	int elapsedTime = (t2.tv_sec - t1.tv_sec) * 1000.0;      // sec to ms
	elapsedTime += (t2.tv_usec - t1.tv_usec) / 1000.0;   // us to ms
	printf("finished to write data in %d milliseconds\n", elapsedTime);
	
	nm_close(d);
}

int main() {
	sender();
}
