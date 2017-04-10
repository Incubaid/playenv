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
unsigned int sleep(unsigned int seconds);
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

for i=1, 1000 do
	sem_mutex:dec()
	if shm_data.capacity == shm_data.length then -- buffer is full
		print("buffer is full at i = ", i)
		sem_mutex:inc()
		ffi.C.sleep(1)
	else
		--print("fill data at ", shm_data.end_idx);
		ffi.C.memset(shm_data.data[shm_data.end_idx], 65 + shm_data.end_idx, 1024)
		shm_data.end_idx = (shm_data.end_idx + 1) % shm_data.capacity;
		shm_data.length = shm_data.length + 1
	
		sem_mutex:inc()
		sem_ring:inc()
	end
end
