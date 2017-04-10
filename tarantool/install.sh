set -ex

apt-get -y update
apt-get install -y git build-essential cmake lua5.1 liblua5.1-0-dev luarocks libssl-dev

mkdir -p /opt/code/varia
cd /opt/code/varia

#  install from git repo
#git clone https://github.com/tarantool/tarantool.git --recursive
#cd tarantool
#apt-get install libreadline-dev
#apt-get install libncurses5-dev
#cmake .
#make
#mkdir -p /usr/share/tarantool
#make install
#cd ..

## install tarantool from tarantool repo
curl http://download.tarantool.org/tarantool/1.6/gpgkey | sudo apt-key add -
release=`lsb_release -c -s`

sudo rm -f /etc/apt/sources.list.d/*tarantool*.list
sudo tee /etc/apt/sources.list.d/tarantool_1_6.list <<- EOF
deb http://download.tarantool.org/tarantool/1.6/ubuntu/ $release main
deb-src http://download.tarantool.org/tarantool/1.6/ubuntu/ $release main
EOF

## install tarantool debugger
sudo apt-get update
sudo apt-get -y install tarantool tarantool-dev tarantool-luaossl

git clone --recursive https://github.com/Sulverus/tdb 
cd tdb 
make 
sudo make install prefix=/usr/share/tarantool/
cd ..

## capnproto support
apt-get install -y capnproto

git clone http://luajit.org/git/luajit-2.0.git
cd luajit-2.0/
git checkout v2.1
make && sudo make install
ln -sf /usr/local/bin/luajit-2.1.0-beta2 /usr/local/bin/luajit

luarocks install lua-capnproto
luarocks install lua-cjson


## tarantool packages

mkdir -p ~/.luarocks/
cat > ~/.luarocks/config.lua <<EOF
rocks_servers = {
    [[http://rocks.tarantool.org/]]
}
EOF

luarocks install expirationd

luarocks install http --local
luarocks install  connpool
luarocks install queue
luarocks install shard
# luarocks install spmon

rm ~/.luarocks/config.lua

cd /opt/code/varia

## install lua IPC library
cd /opt/code/varia
git clone https://github.com/siffiejoe/lua-luaipc.git
cd lua-luaipc
make LUA_INCDIR=/usr/include/lua5.1
sudo make install DLL_INSTALL_DIR=/usr/local/lib/lua/5.1

## install lightningmdb
cd /opt/code/varia
git clone https://github.com/LMDB/lmdb
cd lmdb/libraries/liblmdb/
make
sudo make install

sudo luarocks install lightningmdb
