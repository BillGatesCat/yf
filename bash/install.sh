#!/bin/bash

cd $(dirname "$0")

sudo apt install pip
pip install pyinstaller
pip install yfinance

git clone https://github.com/sstephenson/bats.git
./bats/install.sh /usr/local

pyinstaller src/main.py --onefile

