local IsaErasure = require("isa_erasure")

local data_shards = 4
local parity_shards = 2
local isa_erasure = IsaErasure.new(data_shards, parity_shards)

function test_encode_decode(filename)
	local data = io.open(filename, "r"):read("*all")
	
	local encoded = isa_erasure:encode(data)
	print("encode OK")

	local ori_blocks = encoded[2]
	encoded[2] = ""
	local broken_idx = {2}
	local recovered = isa_erasure:decode(encoded, broken_idx)
	print("recovery OK")
	print("checking recovered data")
	print("num of recovered data = ", #recovered)
	print("checking recovered = ", recovered[2] == ori_blocks)
	print("len recovered = ", #recovered[2])
	print("len ori blocks = ", #ori_blocks)
	print("ori_blocks = ", string.sub(ori_blocks,1, 10))
	print("recovered = ", string.sub(recovered[2],1, 10))
end

test_encode_decode("luajer.lua")
