#!/bin/bash

python make_data.py -o data/data.csv -n 50 -d 2 --seed 666666
python make_data.py -o data/data.npy -n 100 -d 3 --seed 7777777

