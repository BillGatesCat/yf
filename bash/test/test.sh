echo "Compiling python code..."

cd $(dirname "$0")

git clone https://github.com/sstephenson/bats.git
sudo ./bats/install.sh /usr/local


./../install.sh

cd bats
bats interface.bats
