#!/bin/bash
echo "Enter the choice:"
echo "1->While 2->Until 3->For"
read ch
case $ch in
	1)
		n=1
		while [ $n -le 10 ]
		do
			echo "$n"
			n=`expr $n + 1`
		done;;
	2)
		n=1
		until [ $n -eq 11 ]
		do 
			echo "$n"
			n=`expr $n + 1`
		done;;
	3)
		for (( i=1 ; i<=10 ; i++ ))
		do  
			echo "$i"
		done;;
	*)
		echo "Choice Out Of Bound"
esac
