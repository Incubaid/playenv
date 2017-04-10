# DPDK experiment

Sending `hello` to other computer.

To make it work, we need to modify DEST_MAC0 ..DEST_MAC5 variable
in `single_sender.c`. Change it with your receiver mac address.

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

**single_receiver**

```
sudo ./build/single_receiver -b 0000:00:03.0
```

`-b` option above tolds the dpdk to not use ethernet device with PCI address = `0000:00:03.0`


**single_sender**
```
sudo ./build/single_sender
```
