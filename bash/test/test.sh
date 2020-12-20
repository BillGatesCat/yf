echo "Compiling python code..."

cd ..
./install.sh

cd test/bats
bats interface.bats
