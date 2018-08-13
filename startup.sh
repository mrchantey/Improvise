#!/bin/bash

echo "starting in 10 seconds"


echo "startup python script running..."


cd /

cd home/nao/custom/improvise

python -m pkg.auto_improvise na02.local -d

echo "startup python script terminated..."

#python /home/nao/custom/nurse_nao/nurse_nao.py
