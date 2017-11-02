local IsaErasure = require("isa_erasure")

local data_shards = 4
local parity_shards = 2
local isa_erasure = IsaErasure.new(data_shards, parity_shards)

function test_encode_decode(filename)
	local data = io.open(filename, "r"):read("*all")
	
	local encoded = isa_erasure:encode(data)
	print("encode OK")

	-- simulate first data corrupted
	local corrupt_idx = 1
	local corrupteds = {}
	for i=2, #encoded do
		corrupteds[i-1] = encoded[i]
	end
	for i = 1, #corrupteds do
		assert(corrupteds[i] == encoded[i+1])
	end
	print("encoded len =", #encoded, ", . corrupted len = ", #corrupteds)
	local ori_blocks = encoded[corrupt_idx]
	local broken_idx = {corrupt_idx}
	local recovered = isa_erasure:decode(corrupteds, broken_idx)
	print("recovery finished")
	print("checking recovered data")
	print("num of recovered data = ", #recovered)
	print("checking recovered = ", recovered[1] == ori_blocks)
	print("len recovered = ", #recovered[1])
	print("len ori blocks = ", #ori_blocks)
	print("ori_blocks = ", string.sub(ori_blocks,1, 10))
	print("recovered = ", string.sub(recovered[1],1, 10))
end

test_encode_decode("luajer.lua")
