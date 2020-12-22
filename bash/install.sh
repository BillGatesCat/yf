#!/bin/bash

cd $(dirname "$0")

sudo apt install pip
pip install pyinstaller
pip install yfinance

git clone https://github.com/sstephenson/bats.git
sudo ./bats/install.sh /usr/local

pyinstaller src/main.py --onefile -n yf


mkdir libexec
mkdir bin

cp dist/yf libexec
ln -s ../libexec/yf bin 
