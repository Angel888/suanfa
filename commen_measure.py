# 最大公约数v
def max_common_measure(num_1,num_2):
    if num_1>num_2:
        max_n,min_n=num_1,num_2
    elif num_1<num_2:
        max_n,min_n=num_2,num_1
    else:
        return num_1
    b=max_n-min_n
    return max_common_measure(b,min_n)
print(max_common_measure(8251,6105))
print(max_common_measure(9,6))