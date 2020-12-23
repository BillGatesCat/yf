#!/bin/bash

cd $(dirname "$0")
PREFIX="$1"

rm "$PREFIX/bin/yf"
rm "$PREFIX/libexec/yf"
