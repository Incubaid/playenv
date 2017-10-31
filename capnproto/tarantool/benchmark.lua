local big = require "Big_capnp"
local capnp = require "capnp"

local num_data = 1000 * 1000

-- serialize user data to capnproto
function serialize_data()
	local data = {
		title = "thisnis a unique title ",
		repo = "this is a repo, we should add some data",
        organization = "this is a repo, we should add some data",
        content = "this is a repo, we should add some data",
	}
	return big.Issue.serialize(data)
end


box.cfg {
    listen = 3313,
	memtx_memory = (num_data * 500 )
}

box.once("bootstrap", function()
	print("bootstraping database...")
    box.schema.space.create('tester')
    box.space.tester:create_index('primary',
        { type = 'TREE', parts = {1, 'unsigned'}})
end)



function write_data(num)
  local string_value, t
  for i = 1, num do
    data = serialize_data()
    t = box.tuple.new({i,data})
    box.space.tester:replace(t)
  end
end

function benchmark()
	local start1, start2
	
	local data = serialize_data()
	print('start with memtx_memory = ', box.cfg.memtx_memory / 1024, ' kbytes')
	print('number of data = ', num_data)
	print('length of one data = ', #data, ' bytes')

	start_clock = os.clock()
	
	write_data(num_data)

	local elapsed = (os.clock() - start_clock)

	print(string.format("total time : %10.6f seconds", elapsed))

	local actual_data_size = num_data * #data
	local bin_size = box.space.tester:bsize()

	print("memory overhead = ", bin_size - actual_data_size, " bytes")
end

require('console').start()
