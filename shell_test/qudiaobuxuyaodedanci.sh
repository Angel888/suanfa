#写一个 bash脚本以实现一个需求，去掉输入中的含有B和b的单词
#示例:
#假设输入如下：
#big
#nowcoder
#Betty
#basic
#test
#
#
#你的脚本获取以上输入应当输出：
#nowcoder test
#
#说明:
#你可以不用在意输出的格式，空格和换行都行

#!/usr/bin/env bash
while read lines
do
    for i in ${lines[@]}
    do
        if [[ "$i" =~ b || "$i" =~ B  ]];then
            continue
        fi
        echo $i
    done
done<bb