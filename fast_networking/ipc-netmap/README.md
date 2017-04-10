# netmap pipes example

Netmap pipes works in burst mode, with default TX & RX slots values is 255.

In this example code, we show how to change that values to 100.

## build netmap

```
git clone https://github.com/luigirizzo/netmap.git
cd netmap/LINUX
./configure
make
```

## install netmap kernel module

```
sudo insmod ./netmap.ko
```

## Build the examples

```
cd $THIS_DIRECTORY // then change `CFLAGS += -I /home/vagrant/netmap/sys` in makefile to your netmap dir
make
```

## run the examples

```
sudo ./receiver
```

```
sudo ./sender
```

