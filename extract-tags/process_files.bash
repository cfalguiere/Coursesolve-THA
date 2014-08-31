#!/bin/bash

for f in $(find ../tha-data/ -name "*.csv")
do
        echo $f
	python extract_factors.py $f
done