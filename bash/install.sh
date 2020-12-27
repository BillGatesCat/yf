#!/bin/bash

cd $(dirname "$0")

./clean.sh

pyinstaller src/main.py --onefile -n yf

mkdir libexec bin

cp dist/yf libexec
ln -s ../libexec/yf bin

sudo cp -R ./bin/* /usr/local/bin
sudo cp -R ./libexec/* /usr/local/libexec