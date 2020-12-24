echo "Compiling python code..."

cd $(dirname "$0")

pyinstaller ../src/main.py --onefile -n yf

bats bats/interface.bats

echo "Cleaning up artifacts..."
rm -rf build dist yf.spec