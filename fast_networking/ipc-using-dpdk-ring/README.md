# IPC using DPDK ring library

## Lua example


Sender send 10K `hello` to receiver.

There are some works for using dpdk from Lua:

- need to compile dpdk as shared variable. 
  To do it, set `CONFIG_RTE_BUILD_SHARED_LIB=y` in 
  `config/common_base`

- export these functions : rte_mempool_get, rte_mempool_put, rte_ring_enqueue, rte_ring_dequeue.
  To do it:
  		- for each function, create new exported function with prefix `2`
		- add newly created function to `rte_[libmame]_version.map` file


It seems we don't really need above workarounds because MoonGen seems doesn't need it.

##Running Lua example

start the receiver
```
sudo tarantool receiver.lua
```

start the sender
```
sudo tarantool sender.lua
```
## C example

see http://dpdk.org/doc/guides/sample_app_ug/multi_process.html#basic-multi-process-example

Snippet of the code to send a message

```
if (rte_mempool_get(message_pool, &msg) < 0)
	rte_panic("Failed to get message buffer\n");
	
snprintf((char *)msg, string_size, "%s", res->message);

if (rte_ring_enqueue(send_ring, msg) < 0) {
	printf("Failed to send message - message discarded\n");
	rte_mempool_put(message_pool, msg);
}
```

receive message
```
while (!quit){
   void *msg;
	if (rte_ring_dequeue(recv_ring, &msg) < 0){
		usleep(5);
		continue;
	}
   printf("core %u: Received '%s'\n", lcore_id, (char *)msg);
   rte_mempool_put(message_pool, msg);
}
```
