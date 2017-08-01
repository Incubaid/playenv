#!bash
set -ex
export builddir=/tmp/protoc
mkdir -p $builddir
pushd $builddir
wget https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
unzip proto*
cp bin/protoc /usr/local/bin/
popd
bash generate.sh
