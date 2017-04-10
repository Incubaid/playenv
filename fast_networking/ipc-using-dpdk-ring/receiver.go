package main

// #cgo LDFLAGS: -lrte_eal -lrte_mempool -lrte_ring
// #include <dpdk/rte_config.h>
// #include <dpdk/rte_eal.h>
import "C"

func main() {
	argc := C.int(1)
	argv := make([]*C.char, 1)
	argv[0] = C.CString("receiver")
	C.rte_eal_init(argc, &argv[0])
}
