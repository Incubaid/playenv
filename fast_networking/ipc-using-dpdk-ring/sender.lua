local ffi = require("ffi")
local dpdkc = require "dpdkc"

ffi.cdef[[
// eal init
int rte_eal_init(int argc, const char* argv[]);
unsigned 	rte_socket_id (void);
enum rte_proc_type_t 	rte_eal_process_type (void);

// rte_ring
struct rte_ring *rte_ring_lookup (const char *name);
int rte_ring_enqueue2(struct rte_ring *r, void *obj);

// mempool
struct rte_mempool * 	rte_mempool_lookup (const char *name); 
int rte_mempool_get2(	struct rte_mempool * 	mp,void ** 	obj_p);
void 	rte_mempool_put2 (struct rte_mempool *mp, void *obj);

void *malloc(size_t size);
char *strcpy(char *dest, const char *src);
char *strncpy(char *dest, const char *src, size_t n);
int usleep(int usec);
]]


local RING_NAME = "the_ring"
local POOL_NAME = "the_pool"

local eal = ffi.load("rte_eal", true)
local mempool = ffi.load("rte_mempool", true)
local ring = ffi.load("rte_ring", true)

local argv = {"luajit", "receiver.lua", "--proc-type=secondary"}
local argc = #argv

assert(eal.rte_eal_init(argc, ffi.new("const char*[?]", argc, argv)))

-- ring init
local the_ring = ring.rte_ring_lookup(RING_NAME)
assert(the_ring)

-- mempool
local the_pool = mempool.rte_mempool_lookup(POOL_NAME)
assert(the_pool)

-- start sender
print("starting sender")
local TO_SEND = 10000
local sent = 0
while sent < TO_SEND do
	local msg = ffi.new("char*[1]")

	if mempool.rte_mempool_get2(the_pool, ffi.cast("void **", msg)) < 0 then
		print("failed to get message")
		os.exit(1)
	else
		ffi.C.strcpy(msg[0], "hello")
		if ring.rte_ring_enqueue2(the_ring, msg[0]) < 0 then
			print("failed to send message at  = ",sent)
			mempool.rte_mempool_put2(the_pool, msg[0])
			ffi.C.usleep(10)
		else
			sent = sent + 1
		end
	end
end
print("sender finished to write ", TO_SEND)
