#!/usr/bin/env bash
#todo 我的和答案到底有什么区别？？？
while read linestr
do
    if [ ! -z $linestr ];then
    echo $linestr
    fi
done < nowcoder.txt

#---------------
#!/bin/bash
while read line
do
  if [ ! -z $line ]
  then
     echo $line
  fi
done < nowcoder.txt