local turbo = require "turbo"

local _M = { _VERSION = '0.01' }

local PASSWD = "the_password"

local AuthHandler = class("AuthHandler", turbo.web.RequestHandler)

-- handle login request
-- it return the token which is username of the user
function AuthHandler:post()
	local data = self:get_json()
	
	if data["password"] ~= PASSWD then
		self:set_status(401)
		self:write({error = "Unauthorized"})
		print("password=", data["password"])
		return
	end
	self:set_status(200)
	self:write({token = data["username"]})
end

function check_token(req)
	local hdr = req.headers:get("Authorization", true)
	if hdr == nil then
		hdr = ""
	end
	return hdr
end

_M.AuthHandler = AuthHandler

return _M
