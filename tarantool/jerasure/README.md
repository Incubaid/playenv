# Jerasure in Tarantool

## Install

We need to install jerasure2 C library

```
bash install_jerasure2_c_lib.sh
```

## tarantool-lua-jerasure modules

There are two Lua files which gives jerasure in tarantool support:

- **luajer.lua**

It is Lua binding for C jerasure module from https://github.com/tsuraan/Jerasure.

It can be used in Luajit & Tarantool environment.

`test_luajer.lua` is test file for `luajer.lua`.

- **tarantool_jerasure.lua**

It is simple module to save erasure coded file to tarantool.

It still doesn't handle corrupted devices.

Value of k (number of data devices) and m (number of coding devices) still hardcoded
to k=10 and m=2.

It works by:

	- erasure coded the file
	- split resulted 12 file pieces to different spaces (jer_1, jer_2.....jer_12)

`test_tarantool_jerasure.lua` is test file for `tarantool_jerasure.lua`

## Simple Binary file Server 

`jerhttp.lua` is http file binary file server build for this test.


## test procedure

To get better result it is better to do these steps when testing:

- clean & initialize database (there is already guide & script below)
- do write/upload test
- do read/download test
- clean & init database before doing another write-read test

**Server side**

clean old database 

```
bash clean.sh
```

Initialize database

```
tarantool init.lua
```

Start http server

```
tarantool jerhttp.lua
```

**client side**

Test client written using Go, for upload operation, it will upload file named `payload` in 
current directory.

compile test client

```
go build
```

200x parallel upload operation using 5 goroutines (each goroutine do 40 upload)

```
./jerasure -num=200 -mode=save_parallel
```

Each operation will do upload to different ID (1-200).

To do serial upload, change `mode` option from `save_parallel` to `save_serial`.

To increase number of upload operation to 1000, change `num` option from 200 to 1000.


200x parallel get operation using 5 goroutines (each goroutine do 40 get/download)

```
./jerasure -num=200 -mode=get_parallel
```

Each operation will download from different ID (1-200).

To do serial download, change `mode` option to `get_serial`

## nginx reverse proxy

there is nginx.conf that proxied the jerhttp.lua server.

To do test using nginx:

- cp nginx.conf /etc/nginx/conf.d/jerhttp.conf
- /etc/init.d/nginx restart
- add `-via_nginx=true` option when executing client
