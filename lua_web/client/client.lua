local cjson = require "cjson"
local hc = require("httpclient").new()

local base_uri = "http://localhost:5000"
local TOKEN = ""

-- login using username & password
function login(username, password)
	local body = cjson.encode({username = username, password = password})
	local res = hc:post(base_uri .. '/auth', body, {content_type = "application/json"})

	if res.code ~= 200 then
		return {code=res.code}
	end
	
	local decoded = cjson.decode(res.body)
	
	TOKEN = decoded["token"]
	
	return {token = decoded["token"], code=res.code}
end

-- create user
function create_user(username, name)
	local body = cjson.encode({username = username, name = name})
	local res = hc:post(base_uri ..'/users', body, {headers = {Authorization = TOKEN}, content_type = "application/json"})
	return {code = res.code}
end

-- get a user detail
function get_user(username)
	local res = hc:get(base_uri .. "/users/" .. username, {headers = {Authorization = TOKEN}})
	return cjson.decode(res.body)
end

-- get all users
function get_all_users()
	local res = hc:get(base_uri .. "/users", {headers = {Authorization = TOKEN}})
	return cjson.decode(res.body)
end


print("login")
local ret = login("johndoe", "the_password")
print('code = ', ret['code'], 'token=', ret['token'])

print("create user")
local ret = create_user("bill", "Bill Murray")
print("create_user result code =", ret["code"])
local ret = create_user("john", "John Doe")
print("create_user result code =", ret["code"])

print("get back user data")
local user = get_user("bill")
print("user = ", user["username"], ". name = ", user["name"])

local users = get_all_users()
for i=1, #users do
	print(users[i]["username"], "=>", users[i]["name"])
end
