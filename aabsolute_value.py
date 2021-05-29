import sys
MAX_INT=sys.maxsize
def absolute_value(l_list):
    """
    按照绝对值进行排序，相邻的两个相加
    :param l_list:
    :return:
    """
    l=len(l_list)
    def change_to_posivite(numm):
        if numm<0:
            numm=-numm
        return numm
    absolute_real=list(map(lambda x:(change_to_posivite(x),x),l_list))
    absolute_real.sort(key=lambda x:abs(x))
    print(absolute_real)
    min_sum=MAX_INT
    for i in range(l-1):
        tmp=abs(absolute_real[i][1]+absolute_real[i+1][1])
        if tmp<min_sum:
            min_sum=tmp
    print(min_sum)
    return min_sum
if __name__ == '__main__':
    absolute_value([1, 4, 6])