# Lua REST Server Tutorial

In this tutorial we will build a simple REST server with [turbolua](http://turbolua.org).

It is implementation of api.raml found in `docs/tutorial` directory of go-raml repo, without
the itsyou.online integration, because there is currently no Lua JWT which have ECDSA support
used by itsyou.online.

As for now, client simply send username+password and server give back token which need to be used
in authenticated requests.


## Server

Install required packages
```
$ apt-get install luarocks git build-essential libssl-dev
$ luarocks install turbo
```

Run the server
```
cd server
luajit main.lua
```

You can replace `luajit` above with `tarantool` to run it inside tarantool environment.

## Client

Install required packages

`sudo luarocks install httpclient`

Run client

```
cd client
luajit client.lua
```

## Memory usage

**startup**
Memory usage of the server app  measured using `pmap` in startup is 28432K.
As comparison, a hello world [Flask](http://flask.pocoo.org/) need  79964K.

**load tested**

tested with ab using this command
```
ab -n 100000 -c 10 -H "Authorization: petok" http://127.0.0.1:5000/users/bill
```

memory usage measured using `pmap` is 30648K.


