#!/bin/sh
echo "enter the number:"
read a
if [ `expr $a % 2` -eq 0 ] 
then
echo "$a is even"
else
echo "$a is odd"
fi
