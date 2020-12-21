#!/bin/bash

cd $(dirname "$0")

sudo apt install pip
pip install pyinstaller
pip install yfinance


pyinstaller src/main.py --onefile
