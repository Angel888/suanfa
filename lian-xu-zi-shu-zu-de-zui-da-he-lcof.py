# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums) :
        l=len(nums)
        if l==0:
            return 0
        res=nums[0]
        max_n=nums[0]
        for i in range(1,l):
            res=max(nums[i],res+nums[i]) #todo res只是到这里最大的数，max_n是所有结果中最大的数
            max_n=max(res,max_n)

# -2
# 4
# 3
# 5
# 6
# 1
# 5
# 5
        return max_n

    def maxSubArray1(self, nums) -> int:
        for i in range(1, len(nums)):
            # nums[i] += max(nums[i - 1], 0)
            nums[i] =nums[i]+ max(nums[i - 1], 0)
        print(nums)  #[-2, 1, -2, 4, 3, 5, 6, 1, 5]
        return max(nums)


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
































