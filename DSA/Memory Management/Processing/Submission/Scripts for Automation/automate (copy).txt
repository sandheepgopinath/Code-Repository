#!/bin/bash

# To generate the input
python input_restriction.py -n 27

# To process the data
python dsa.py -o const
python dsa.py -o lin
python dsa.py -o quad
python dsa.py -o cube -t 5
python dsa.py -o log
python dsa.py -o exp -t 5

#To plot the graphs
python dsaplot.py

