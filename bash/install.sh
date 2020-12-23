#!/bin/bash

cd $(dirname "$0")

./clean.sh

apt install pip
pip install "pyinstaller>=4.0,<5.0"
pip install yfinance==0.1.55
git clone https://github.com/sstephenson/bats.git
./bats/install.sh /usr/local

pyinstaller src/main.py --onefile -n yf

mkdir libexec bin

cp dist/yf libexec
ln -s ../libexec/yf bin

cp -R ./bin/* /usr/local/bin
cp -R ./libexec/* /usr/local/libexec