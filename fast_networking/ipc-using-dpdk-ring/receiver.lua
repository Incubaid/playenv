local ffi = require("ffi")
local dpdkc = require "dpdkc"

ffi.cdef[[
// eal init
int rte_eal_init(int argc, const char* argv[]);
unsigned 	rte_socket_id (void);
enum rte_proc_type_t 	rte_eal_process_type (void);

// rte_ring
struct rte_ring* rte_ring_create(const char * name,unsigned count,int socket_id,unsigned flags);
int rte_ring_dequeue2 (struct rte_ring *r, void **obj_p);

// mempool
typedef void (rte_mempool_ctor_t)(struct rte_mempool *, void *);
typedef void (rte_mempool_obj_ctor_t)(struct rte_mempool *, void *, void *, unsigned);
struct rte_mempool * rte_mempool_create (const char *name, unsigned n, unsigned elt_size, unsigned cache_size, unsigned private_data_size, rte_mempool_ctor_t *mp_init, void *mp_init_arg, rte_mempool_obj_ctor_t *obj_init, void *obj_init_arg, int socket_id, unsigned flags);
void 	rte_mempool_put2 (struct rte_mempool *mp, void *obj);

void *malloc(size_t size);
char *strcpy(char *dest, const char *src);
int usleep(int usec);
]]


local RING_NAME = "the_ring"
local RING_SIZE = 256
local RING_FLAGS = 0
local POOL_NAME = "the_pool"
local POOL_SIZE = 1024
local STRING_SIZE = 64
local POOL_CACHE = 32
local PRIV_DATA_SZ = 0
local POOL_FLAGS = 0

local eal = ffi.load("rte_eal", true)
local mempool = ffi.load("rte_mempool", true)
local ring = ffi.load("rte_ring", true)

local argv = {"luajit", "receiver.lua", "--proc-type=primary"}
local argc = #argv

assert(eal.rte_eal_init(argc, ffi.new("const char*[?]", argc, argv)))

-- ring init
local the_ring = ring.rte_ring_create(RING_NAME, RING_SIZE, eal.rte_socket_id(), RING_FLAGS)

-- mempool
local the_pool = mempool.rte_mempool_create(ffi.new("char [?]", #POOL_NAME, POOL_NAME), POOL_SIZE, STRING_SIZE, POOL_CACHE, PRIV_DATA_SZ,
										nil, nil, nil, nil,
										eal.rte_socket_id(), POOL_FLAGS)

-- start receiver
print("starting receiver")
local TO_RECV = 10000
local recvd = 0
while recvd < TO_RECV do
	local msg = ffi.new("char*[1]")
	if ring.rte_ring_dequeue2(the_ring, ffi.cast("void **", msg)) < 0 then
		ffi.C.usleep(5)
	else
		recvd = recvd + 1
		print("msg["..recvd.."] = ".. ffi.string(msg[0]))
		mempool.rte_mempool_put2(the_pool, msg[0])
	end
end
