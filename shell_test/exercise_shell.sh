#https://www.nowcoder.com/practice/2c5a46ef755a4f099368f7588361a8af?tpId=195&tqId=36223&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fshell%2Fquestion-ranking&tab=answerKey
#!/usr/bin/env bash
#假设输入如下：
#that is your bag
#is this your bag?
#to the degree or extent indicated.
#there was a court case resulting from this incident
#welcome to nowcoder
#todo 哪里错了？
sub="this"
while read linestr
do
    flag=1
    for a in ${linestr[@]}
    do
        if [ $a == $sub ];then  #这里的【】和字符之间要有间距  ==要有两边要有空格
            flag=0 #todo 这里为啥要让我转换？为啥不是$flag?
            break
        fi
    done
#    if [ $flag -eq 1 ];then
    if [[ $flag -eq 1 ]];then
        echo $linestr
    fi
done<nowcoder.txt
#---------------
sub="this"
while read linestr
do
    flag=1
    for a in ${linestr[@]}
    do
        if [ $a == $sub ];then
           flag=0  #todo
           break
        fi
    done
    if [ $flag -eq 1 ];then
        echo $linestr
    fi

done<nowcoder.txt