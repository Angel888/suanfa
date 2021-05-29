#!/usr/bin/env bash
#grep -P ^(\d{3} | \d \{3}\d)
i=1
a=0
#while [[ $i -lt 101 ]]
#do
#a=$(($a+$i))
#i=$(($i+1))
#done
#echo $a

for((i=1;i<=100;i++));
do
a=$(($a+$i))
done
echo $a

echo '' | awk '{for(i=1;i<=100;i++){a+=i}}END{print a}'