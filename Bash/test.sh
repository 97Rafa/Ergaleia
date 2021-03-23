#!/bin/bash
read -p "Type a floating number :" number
if [ $(echo "$number>50"| bc) -eq 0 ]; then  
echo "Number than you mentioned in smaller than 50"
else
echo "Number than you mentioned in greater than 50"
fi
