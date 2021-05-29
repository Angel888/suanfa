# https://leetcode-cn.com/problems/maximum-subarray/
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    # Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    Solution().maxSubArray([-2, 1])
