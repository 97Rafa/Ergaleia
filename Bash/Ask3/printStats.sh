#!/bin/bash

for str
do
    var=$1  #pernaei to onoma tou arxeio stin metavliti var
    shift   #paei sto epomeno arxeio

    min=10000.0
    max=-10000.0
    lines=0

    exec<"$var"
    while IFS= read -r line
    do
        let "lines = lines + 1"
        if [ "${line%.*}" -gt "${max%.*}" ]; then
            max=$(echo "scale=1; ${line}"| bc)
        fi

        if [ "${line%.*}" -lt "${min%.*}" ]; then
            min=$(echo "scale=1; ${line}"| bc)
        fi


    done

    echo "FILE:$var,lines:$lines,max=$max,min=$min"

done