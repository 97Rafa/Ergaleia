#!/bin/bash
for str
do
    var=$1  #pernaei to onoma tou arxeio stin metavliti var
    shift   #paei sto epomeno arxeio
    [ -e temp.txt ] && rm temp.txt
    touch temp.txt
    cp "$var" temp.txt

    old_ifs="$IFS"
    COLUMN=1
    sum=0
    col1_sum=0;
    col2_sum=0;

    exec< temp.txt
    while IFS=':' read -r col1 col2
    do	
        let "col1_sum = col1_sum + ${col1}"
        let "col2_sum = col2_sum + ${col2}"

    done 
    IFS="$old_ifs"

    if [ "$col1_sum" -gt "$col2_sum" ]
    then
        let "COLUMN = 1"
        let "sum = col1_sum"
    elif [ "$col2_sum" -gt "$col1_sum" ]
    then
        let "COLUMN = 2"
        let "sum = col2_sum"
    fi


    echo "FILE:$var,COLUMN:$COLUMN,sum=$sum"
done
