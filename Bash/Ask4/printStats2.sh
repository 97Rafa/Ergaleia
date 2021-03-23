#!/bin/bash

for str
do
    var=$1  #pernaei to onoma tou arxeio stin metavliti var
    shift   #paei sto epomeno arxeio

    min=10000.0
    max=-10000.0
    lines=0
    arr=()
    t=0.0;

    exec<"$var"
    while IFS= read -r line #xwrizei me to keno
    do
        arr[lines]=$(echo "scale=1; ${line}"| bc)
        let "lines = lines + 1"

    done

    
    for x in ${arr[@]}
    do
    t=$(echo "scale=1; $x"| bc)
        if [ "${t%.*}" -gt "${max%.*}" ]; then
            max=$(echo "scale=1; $x"| bc)
        fi

        if [ "${t%.*}" -lt "${min%.*}" ]; then
            min=$(echo "scale=1; $x"| bc)
        fi
    done

    echo "FILE:$var,lines:$lines,max=$max,min=$min"

done