-- Jerasure HTTP server
-- it serve binary file by coded it with erasure codes with k = 10 and m = 2
-- and then distribute the encoded part to 12 spaces
local ffi = require("ffi")
local tarjer = require("tarantool_jerasure")

httpd = require('http.server').new('0.0.0.0', 8080)

box.cfg{
	--slab_alloc_maximal = 1048280
}

local j1 = box.space.jer_1
local j2 = box.space.jer_2
local j3 = box.space.jer_3
local j4 = box.space.jer_4
local j5 = box.space.jer_5
local j6 = box.space.jer_6
local j7 = box.space.jer_7
local j8 = box.space.jer_8
local j9 = box.space.jer_9
local j10 = box.space.jer_10
local j11 = box.space.jer_11
local j12 = box.space.jer_12

local K = 10
local M = 2

local jtable  = {j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12}

local function save(req)
	local id = req:stash("id")
	local body = req:read()
	tarjer:save(jtable, K, M, id, body)
end

local function get(req)
	local id = req:stash("id")
	local decoded = tarjer:get(jtable,K, M, id)
	local resp = req:render({text = decoded })
	return resp
end



httpd:route({path = '/put/:id'}, save)
httpd:route({path = '/get/:id'}, get)

print("starting jerhttp server")
httpd:start()
