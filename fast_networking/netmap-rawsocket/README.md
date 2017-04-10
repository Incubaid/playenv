# Fast Networking Experiment with netmap 

Sending `hello` to netmap receiver

## netmap_receiver.c

Simple packet receiver using netmap.

steps:

- Need to configure [netmap](https://github.com/luigirizzo/netmap/blob/master/LINUX/README) first.
- cd $NETMAP_SOURCE_DIR/examples/
- put this file in `examples` directory.
- modify `GNUMakefile` to also compile this file
- `make`


## raw_eth_send.c

sending raw ethernet frame.

To use it, we need to change hardcoded destination mac address & interface


## raw_eth_recv.c

receive raw ethernet frame.

To use it, we need to change hardcoded destination mac address & interface
