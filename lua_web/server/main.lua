local turbo = require "turbo"
local cjson = require "cjson"

-- local modules
local auth = require "auth"

-- global users map
local users = {}

-- /users endpoint handler class
local UsersHandler = class("UsersHandler", turbo.web.RequestHandler)

-- handle GET /users
function UsersHandler:get()
	-- check token
	if string.len(check_token(self.request)) == 0 then
		error(turbo.web.HTTPError(401, "Unauthorized"))
	end
	
	-- create array from users map 
	local arr = {}
	for k, v in pairs(users) do
		arr[#arr + 1] = v
	end

	self:write(arr)
end

-- handle POST /users
-- it simply save to global in-memory users table
function UsersHandler:post()
	-- check token
	if string.len(check_token(self.request)) == 0 then
		error(turbo.web.HTTPError(401, "Unauthorized"))
	end
	
	-- decode request
	local user = self:get_json()

	-- save to our in-memory DB
	users[user["username"]] = user
	
	self:set_status(201)
    self:write({})
end

-- /users/{username} endpoint handler class
local UserDetailHandler = class("UserDetailHandler", turbo.web.RequestHandler)
function UserDetailHandler:get(username)
	if string.len(check_token(self.request)) == 0 then
		error(turbo.web.HTTPError(401, "Unauthorized"))
	end
    self:write(users[username])
end

-- create turbo app
local app = turbo.web.Application:new({
	{"/users/(.*)$", UserDetailHandler},
    {"/users", UsersHandler},
	{"/auth", auth.AuthHandler}
})

-- listen on port 5000
app:listen(5000)

-- start the turbo event loop
turbo.ioloop.instance():start()
