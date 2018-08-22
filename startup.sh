#!/bin/bash

# echo "starting in 10 seconds"


echo "startup python script running..."


cd /

cd home/nao/improvise

# python -m pkg.auto_improvise na01.local 5000 -d
python -m pkg.auto_improvise na02.local 5001 -d

echo "startup python script terminated..."

