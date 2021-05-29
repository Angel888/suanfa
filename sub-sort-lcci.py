# https://leetcode-cn.com/problems/sub-sort-lcci/  todo 部分排序
# 输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。
# 注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。
# 方法一:
# 1 整个排好序，从前面遍历，从后面遍历，看从哪里对不上
class Solution:
    # def subSort(self, array):
    #     a = 0
    #     b = 1
    #     d = len(array)-1
    #     c = d-1
    #
    #     while array[a] < array[b]:
    #         a += 1
    #         b += 1
    #     while array[c] < array[d]:
    #         c -= 1
    #         d -= 1
    #     if a>0:
    #         l = [b + 1, d]
    #         print(l)
    #         return l
    #     while array[a] > array[b]:
    #         a += 1
    #         b += 1
    #     while array[c] > array[d]:
    #         c -= 1
    #         d -= 1
    #     if a > 0:
    #         l = [b + 1, d]
    #         print(l)
    #         return l
    def subSort1(self, array):
        a = len(array)
        if a <= 0:
            return [-1, -1]
        array_1 = sorted(array)
        i = 0
        j = a - 1
        while array[i] == array_1[i] and i < a - 1:
            i += 1

        while array[j] == array_1[j] and j >= 0:
            j -= 1
        if a - 1 > i > 0 or a - 1 > j > 0:
            # print(i,j)
            return [i, j]
        i = 0
        j = a - 1
        while array[i] == array_1[-i - 1] and i < a - 1:
            i += 1
        if i == a - 1:
            return [-1, -1]
        while array[j] == array_1[-j - 1] and j >= 0:
            j -= 1
        # print([i, j])
        if a - 1 > i > 0 or a - 1 > j > 0:
            return [i, j]
        return [-1, -1]


if __name__ == '__main__':
    # Solution().subSort1([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    # Solution().subSort1([1, 3, 5, 7, 9])
    Solution().subSort1([5,3,1,7,9])
