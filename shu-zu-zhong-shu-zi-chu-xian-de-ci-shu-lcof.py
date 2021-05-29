import functools


class Solution:
    def singleNumbers(self, nums) :
        ret = functools.reduce(lambda x, y: x ^ y, nums)  # 异或的结果是只剩下出现一次的数
        div = 1
        while div & ret == 0:  # mask这个位号表示的是那两个不重复数的二进制
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]


