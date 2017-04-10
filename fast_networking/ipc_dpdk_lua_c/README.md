# IPC + DPDK experiment

Sending 1000 1024 bytes of data to other computer using dpdk, semaphore, simple ring buffer, & shared memory via ethernet network.

**for most updated version of using shared mem + semaphore, see https://github.com/gig-projects/playenv/tree/master/tarantool/ipc**

## TODO 

TODO:

- Flow control : if receiver processor is too slow, old data in ring buffer will be overwritten by new data
- Destination mac address still hardcoded in dpdk/single_sender.c (you need to modify it when running your test)
- Data length still hardoced in the source 


## Data Flow

lua_sender.lua ---------> [shared mem + semaphore]------>  dpdk/single_sender -----> [ ethernet network ] 

[ethernet network] ---------->  dpdk/single_receiver ----->  [shared mem + semaphore ]------> receiver.lua

lua_sender.lua sending 1000 1024 bytes string

receiver.lua receive the string and write it to result.txt


## setup DPDK

```
./tools/setup.sh
press 14 to compile to x86_64-native-linuxapp-gcc
press 17 to Insert IGB UIO module
press 18 to Insert VFIO module
press 20 to Setup hugepage mappings for non-NUMA systems
press 22 to see your current ethernet device settings
--- you need to take deactivate ethernet device you want to use ---
press 23 Bind Ethernet device to IGB UIO module

```

## Build it

Go to `single_receiver` and `single_sender` directory and do this
```
export RTE_SDK=$PATH_TO_DPDK_DIRECTORY
export RTE_TARGET=x86_64-native-linuxapp-gcc
make
```

## Run

**receiver**

single_receiver
```
cd dpdk_receiver
sudo ./build/single_receiver
```

lua_sender
```
sudo luajit lua_sender.lua
```


**sender**
single_sender.

To make it work, we need to modify DEST_MAC0 ..DEST_MAC5 variable
in `single_sender.c`. Change it with your receiver mac address.
```
sudo ./build/single_sender
```

receveiver.lua
```
sudo luajit receiver.lua
```
