echo "Compiling python code..."

cd ..
./install.sh

cd test/bats
bats interface.bats

cd ../..
echo "Cleaning up pyinstaller output..."
rm -r dist build
rm main.spec
