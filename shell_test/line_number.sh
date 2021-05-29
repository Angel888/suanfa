#!/usr/bin/env bash
i=1
while read linestr
do
    if [ -z $linestr ];then  #注意换行
        echo $i
    fi
i=$(1+$i) #
done<nowcoder.txt
awk ''
