#!/bin/bash
echo "Start"
for i in {3..9}
do
    python3 Inserdata.py $i &
done
