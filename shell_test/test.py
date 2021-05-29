import functools

with open('bb', 'r') as f:
    data = f.readlines()
    print(data)
    data = sorted(data, key = functools.cmp_to_key(lambda x,y: 1 if len(x)> len(y) else -1))
    print(data)


# todo https://www.cnblogs.com/apeway/p/10764597.html  数组中未出现的最小正整数
def smallest_num(num_list):
    num_list.sort()
    for i in num_list:
        tmp=0
        if i>1:
            res=1
            return 1
        elif
