#define NETMAP_WITH_LIBS
#include <net/netmap_user.h>
#include <poll.h>
#include <stdio.h>
#include <string.h>
#include <netinet/ether.h>
#include <arpa/inet.h>

#include "test.h"

void use_data(unsigned char *buf, uint32_t len);

void receiver(void)
{
	struct	nm_desc	*d;
	struct	pollfd fds;
	u_char	*buf;
	struct	nm_pkthdr h;
	
	/**
	 * Opening netmap device as slave
	 * It is actually very simple to open it slave, simply using below line
	 *			d = nm_open("netmap:eth1}0", NULL, 0, 0);
	 *
	 * but we want to show how to change tx_slots & rx_slots value below
	 */
	struct nmreq req;
	bzero(&req, sizeof(req));
	req.nr_tx_slots = TX_SLOTS;
	req.nr_rx_slots = RX_SLOTS;
	req.nr_arg1 = 0;
	req.nr_arg2 = 1;
	req.nr_flags = NR_REG_PIPE_SLAVE;
	d = nm_open("netmap:eth1}0", &req, 0, 0);
	if (d == NULL) {
		perror("failed to open");
		exit(1);
	}

	print_nmreq(d->req);

	fds.fd	= NETMAP_FD(d);
	fds.events = POLLIN;
	int i = 0;
	for (i = 0;i < TO_SEND -1 ;i++) {
		buf = nm_nextpkt(d, &h);
		if (buf == NULL) {
			i--;
			poll(&fds,	1, -1);
			continue;
		}
		use_data(buf, h.len);
	}
	printf("got %d data\n", TO_SEND);
	fflush(stdout);
	nm_close(d);
}



void use_data(unsigned char *buf, uint32_t len) {
	unsigned char data[1024];
	
	memcpy(data, buf , (len < 1024) ? len : 1024);
}
int main() {
	receiver();
}

