set -ex


curl http://download.tarantool.org/tarantool/1.7/gpgkey | sudo apt-key add -
release=`lsb_release -c -s`

# install https download transport for APT
apt-get -y install apt-transport-https

# append two lines to a list of source repositories
rm -f /etc/apt/sources.list.d/*tarantool*.list
tee /etc/apt/sources.list.d/tarantool_1_7.list <<- EOF
deb http://download.tarantool.org/tarantool/1.7/ubuntu/ $release main
deb-src http://download.tarantool.org/tarantool/1.7/ubuntu/ $release main
EOF

# install
apt-get update
apt-get -y install tarantool

pushd $TMPDIR
git clone http://luajit.org/git/luajit-2.0.git
cd luajit-2.0/
git checkout v2.1
make && sudo make install
ln -sf /usr/local/bin/luajit-2.1.0-beta3 /usr/local/bin/luajit
popd

pushd $TMPDIR
git clone --recursive https://github.com/Sulverus/tdb
cd tdb
make
make install prefix=/usr/lib/tarantool/

tarantoolctl rocks install shard
tarantoolctl rocks install document
tarantoolctl rocks install prometheus
tarantoolctl rocks install queue
tarantoolctl rocks install expirationd
tarantoolctl rocks install connpool
tarantoolctl rocks install http

apt install luarocks
luarocks install redis-lua
luarocks install yaml
luarocks install penlight
luarocks install luasec
luarocks install luatweetnacl
luarocks install lua-cjson
luarocks install luafilesystem
luarocks install siphash --from=http://mah0x211.github.io/rocks/

apt install libsodium-dev
luarocks install symmetric

#NEED TARANTOOL INSTALL

popd
