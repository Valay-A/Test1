#!/bin/bash
sed -z "s/n_iter/n_iter=$2/" inp-template.py > inp-template1.py
sed -z "s/eta/eta=$1/" inp-template1.py > inp.py
python main.py > result.dat
tail -1 result.dat
