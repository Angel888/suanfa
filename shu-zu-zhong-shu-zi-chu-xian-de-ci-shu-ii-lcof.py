# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
# todo 二进制位？https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
class Solution:
    def singleNumber(self, nums) -> int:
        a=[]
        for i in nums:
# todo