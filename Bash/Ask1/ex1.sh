#!/bin/bash

cat /usr/include/stdio.h

awk '{print $3,$4,$5,$6}'  /usr/include/stdio.h

touch output.4col | cut -d ":" -f 1,2 input.4col --output-delimiter='        ' > output.4col | cut -d "-"  -f 1,2,3 output.4col --output-delimiter='        ' > output.4col

sort -k 3 output.4col -o output.4col