# Capnproto on Tarantool

## Tarantool

Install tarantool

```
curl http://download.tarantool.org/tarantool/1.6/gpgkey | sudo apt-key add -
release=`lsb_release -c -s`

sudo rm -f /etc/apt/sources.list.d/*tarantool*.list
sudo tee /etc/apt/sources.list.d/tarantool_1_6.list <<- EOF
deb http://download.tarantool.org/tarantool/1.6/ubuntu/ $release main
deb-src http://download.tarantool.org/tarantool/1.6/ubuntu/ $release main
EOF

sudo apt-get update
sudo apt-get -y install tarantool git build-essential
```

## capnproto

```
sudo apt-get install capnproto
```


## Luajit

we will use lua-capnproto library which need luajit to run.

```
git clone http://luajit.org/git/luajit-2.0.git
cd luajit-2.0/
git checkout v2.1
make && sudo make install
sudo ln -sf luajit-2.1.0-alpha /usr/local/bin/luajit
```

## lua-capnproto

```
sudo apt-get install lua5.3 luarocks
sudo luarocks install lua-capnproto
sudo luarocks install lua-cjson
```

## simple tarantool stored procedure using lua-capnproto

**create canpnp file**

User.capnp, it is capnproto definition
```
@0x9a7562d859cc7ffa;

struct User {
  id @0 :UInt32;
  name @1 :Text;
}
```

**compile canpnp file**

```
capnpc -olua User.capnp
```

It will produce `User_capnp.lua` file

**Use it as tarantool stored procedure**

We created two functions in serialize_user.lua:

- serialize_user : to serialize user data into capnp
- parse user : parse serialized user data to lua object

```
ubuntu@ubuntu-xenial:~/playenv/capnproto/tarantool$ tarantool
tarantool: version 1.6.8-691-g4ed9d50
type 'help' for interactive help
tarantool> dofile("serialize_user.lua")
---
...

tarantool> bin = serialize_user(1, "john doe")
---
...

tarantool> user = parse_user(bin)
---
...

tarantool> print(user.name)
john doe
---
...

tarantool> print(user.id)
1
---
...

tarantool> 
```
