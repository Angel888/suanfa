#写一个 bash脚本以统计一个文本文件 nowcoder.txt中字母数小于8的单词。
#
#
#
#示例:
#假设 nowcoder.txt 内容如下：
#how they are implemented and applied in computer
#
#你的脚本应当输出：
#how
#they
#are
#and
#applied
#in
#!/usr/bin/env bash
while read lines
do
    for i in ${lines[@]}
    do
#        echo "$i" ${#i}
        if [[ ${#i} -lt 8 ]];then
            echo $i
        fi
    done
done < nowcoder.txt

cat nowcoder.txt | awk '{}'