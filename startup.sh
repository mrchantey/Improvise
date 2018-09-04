#!/bin/bash

# echo "starting in 10 seconds"
echo clearing port 5000
fuser -k 5000/tcp

echo "startup python script running..."


cd /

cd home/nao/improvise

python -m pkg.auto_improvise nao.local -d
#python -m pkg.auto_improvise na02.local -d

echo "startup python script terminated..."

