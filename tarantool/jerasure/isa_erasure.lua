local ffi = require("ffi")
ffi.cdef[[
void *malloc(size_t size);
void free(void *ptr);
void *memcpy(void *dest, const void *src, size_t n);

void gf_gen_cauchy1_matrix(unsigned char *a, int m, int k);
void ec_init_tables(int k, int rows, unsigned char* a, unsigned char* gftbls);
void ec_encode_data(int len, int k, int rows, unsigned char *gftbls, unsigned char **data,
		    unsigned char **coding);
]]

local isal = ffi.load("isal")

local IsaErasure = {}
IsaErasure.__index = IsaErasure

function IsaErasure.new(data_shards, parity_shards)
	local self = setmetatable({}, IsaErasure)

	-- init encoding table
	local c_encode_tab = ffi.cast("unsigned char *", ffi.C.malloc(32 * data_shards * (data_shards+parity_shards)))
	local c_encode_matrix = ffi.cast("unsigned char *", ffi.C.malloc(data_shards * (data_shards + parity_shards)))

	isal.gf_gen_cauchy1_matrix(c_encode_matrix, data_shards+parity_shards, data_shards)
	isal.ec_init_tables(data_shards, parity_shards, c_encode_matrix + (data_shards * data_shards), c_encode_tab);

	ffi.C.free(encode_matrix);

	self.encode_tab = c_encode_tab

	self.data_shards = data_shards
	self.parity_shards = parity_shards
	return self
end

function IsaErasure.encode(self, data)
	local chunk_size = self:get_chunk_size(#data)
	local c_encoded_data = self:allocate_encoded_data(data)
	local c_encoded_parity = self:allocate_encoded_parity(chunk_size)
	
	isal.ec_encode_data(chunk_size, self.data_shards, self.parity_shards, self.encode_tab, c_encoded_data, c_encoded_parity)

	-- copy the result to Lua table
	local encoded = {}
	for i = 1, self.data_shards do
		encoded[i] = ffi.string(c_encoded_data[i-1], chunk_size)
	end
	for i = 1, self.parity_shards do
		encoded[i+self.data_shards] = ffi.string(c_encoded_parity[i-1], chunk_size)
	end
	self:do_free(c_encoded_data, self.data_shards)
	self:do_free(c_encoded_parity, self.parity_shards)
	return encoded
end

-- encode a Lua string
function IsaErasure.allocate_encoded_data(self, data)
	local chunk_size = self:get_chunk_size(#data)
	local encoded_len = chunk_size * self.data_shards

	-- 8 is sizeof(unsigned char **)
	-- TODO : find a way to make it portable
	c_encoded = ffi.cast("unsigned char **", ffi.C.malloc(8 * self.data_shards))

	-- check whether we need to add padding
	local pad_len = encoded_len - #data
	if pad_len > 0 then
		-- TODO find a way to append the padding in more effective way
		for i=1, pad_len do
			data = data .. 0
		end
	end

	local c_data = ffi.cast("unsigned char *", ffi.C.malloc(#data))
	ffi.copy(c_data, ffi.cast("const void *", data), #data)

	
	-- copy data blocks
	-- TODO : find a way without copy
	for i=0, self.data_shards-1 do
		c_encoded[i] = ffi.cast("unsigned char *", ffi.C.malloc(chunk_size))
		ffi.C.memcpy(c_encoded[i], c_data + (i * chunk_size), chunk_size)
	end

	ffi.C.free(c_data)
	return c_encoded
end

function IsaErasure.allocate_encoded_parity(self, chunk_size)
	local c_encoded = ffi.cast("unsigned char **", ffi.C.malloc(self.parity_shards))
	
	-- allocate parity/coding blocks
	for i=0, self.parity_shards-1 do
		c_encoded[i] = ffi.cast("unsigned char *", ffi.C.malloc(chunk_size))
	end
	
	return c_encoded
end

function IsaErasure.do_free(self, data_ptrs, n)
	for i = 0, n-1 do
		ffi.C.free(data_ptrs[i])
	end
	ffi.C.free(data_ptrs)
end

function IsaErasure.get_chunk_size(self, data_len)
	local size = math.floor(data_len / self.data_shards)
	if data_len % self.data_shards > 0 then
		size = size + 1
	end
	return size
end

function IsaErasure.num_data_shards(self)
	return self.data_shards
end

return IsaErasure
