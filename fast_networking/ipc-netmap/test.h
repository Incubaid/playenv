#ifndef __TEST__H
#define __TEST__H

#define NETMAP_WITH_LIBS
#include <net/netmap_user.h>

#define TX_SLOTS 100
#define RX_SLOTS TX_SLOTS
#define TO_SEND (TX_SLOTS * 100)

void print_nmreq(struct nmreq req)
{
	printf("nr_name=%s, nr_version=%d, nr_offset=%d, nr_memsize=%d\n", req.nr_name, req.nr_version, req.nr_offset, req.nr_memsize);
	printf("tx_slots = %d, rx_slots=%d, tx_rings=%d, rx_rings=%d\n", req.nr_tx_slots, req.nr_rx_slots, req.nr_tx_rings, req.nr_rx_rings);
	printf("nr_cmd=%d, nr_ring_id=%d, nr_arg1=%d, arg2=%d, arg3=%d, nr_flags = %d\n", req.nr_cmd, req.nr_ringid, req.nr_arg1, req.nr_arg2, req.nr_arg3, req.nr_flags);
}

#endif
