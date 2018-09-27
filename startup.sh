#!/bin/bash

# echo "starting in 10 seconds"
echo clearing port 5000
fuser -k 5000/tcp

# echo "improvise running in 10 seconds..."

# sleep 10

echo "improvise running now"

cd /

cd home/nao/improvise

python -m pkg.auto_improvise na01.local -d -rest
#python -m pkg.auto_improvise na02.local -d

echo "improvise terminated..."

