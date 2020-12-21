echo "Compiling python code..."

cd $(dirname "$0")

./../install.sh

cd bats
bats interface.bats
