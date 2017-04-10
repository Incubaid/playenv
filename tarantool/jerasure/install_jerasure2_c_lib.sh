# create build dir
mkdir /tmp/jerasure2

# install required packages
sudo apt-get -y install build-essential autoconf libtool git

# install gf-complete, required by jerasure2
cd /tmp/jerasure2
git clone https://github.com/iwanbk/gf-complete.git
cd gf-complete
autoreconf -i ; autoreconf -i && ./configure && make && sudo make install

# install jerasure2 library
cd /tmp/jerasure2
git clone https://github.com/tsuraan/Jerasure.git jerasure2
cd jerasure2
autoreconf --force --install && ./configure && make && sudo make install && sudo ldconfig

# fix some include file
cd /usr/local/include/
sudo ln -s jerasure/galois.h 
