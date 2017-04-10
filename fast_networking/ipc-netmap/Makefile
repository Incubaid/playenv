# For multiple programs using a single source file each,
# we can just define 'progs' and create custom targets.
PROGS	= sender receiver

CLEANFILES = $(PROGS) *.o
NO_MAN=
CFLAGS = -O2 -pipe
CFLAGS += -Werror -Wall -Wunused-function
CFLAGS += -I /home/vagrant/netmap/sys
CFLAGS += -Wextra

LDFLAGS += -lpthread
LDFLAGS += -lrt	# needed on linux, does not harm on BSD

all: $(PROGS)

sender: sender.o
	$(CC) $(CFLAGS) -o sender sender.o

receiver: receiver.o
	$(CC) $(CFLAGS) -o receiver receiver.o

clean:
	-@rm -rf $(CLEANFILES)
