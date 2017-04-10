local semlib = require("ipc.sem")
local shmlib = require("ipc.shm")
local ffi = require("ffi")

ffi.cdef[[
struct shm_data_t {
	char data[10][1024];
	int capacity;
	int length;
	int start; // read index
	int end_idx; // write index
};
void *memset(void *s, int c, size_t n);
]]

local SHM_NAME = "myshm"
local SEM_RING = "sem_ring"
local SEM_MUTEX_RING = "sem_mutex"
local RING_SIZE = 10;

local sem_ring = assert(semlib.open(SEM_RING, 0))
local sem_mutex = assert(semlib.open(SEM_MUTEX_RING, 0))

local shm = assert(shmlib.attach(SHM_NAME))
local shm_data = ffi.cast("struct shm_data_t *", shm:addr())

local res_file = io.open("result.txt", "w")

while true do
	sem_ring:dec() -- wait for the data
	sem_mutex:dec()

	-- use file
	res_file:write(ffi.string(shm_data.data[shm_data.start], 1024), "\n");
	shm_data.start = (shm_data.start + 1) % shm_data.capacity;
	shm_data.length = shm_data.length - 1;

	sem_mutex:inc()
end
