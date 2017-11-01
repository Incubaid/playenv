local IsaErasure = require("isa_erasure")

local data_shards = 4
local parity_shards = 2
local isa_erasure = IsaErasure.new(data_shards, parity_shards)

function test_encode_decode(filename)
	local data = io.open(filename, "r"):read("*all")
	
	local encoded = isa_erasure:encode(data)
	print("encode OK")
end

test_encode_decode("luajer.lua")
