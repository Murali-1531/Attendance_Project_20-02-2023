#!/bin/sh
echo "Enter the a value:"
read a
echo "Enter the b value:"
read b
echo "Enter the choice:"
echo "1-> Add 2-> Sub 3-> Mul 4-> Div 5-> Mod"
read ch
case $ch in 
	1)echo `expr $a + $b`;;
	2)echo `expr $a - $b`;;
	3)echo `expr $a \* $b`;;
	4)echo `expr $a / $b`;;
	5)echo `expr $a % $b`;;
	*)echo "Enter the correct choice"
esac		
