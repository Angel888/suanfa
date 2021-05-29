# https://leetcode-cn.com/problems/partition-equal-subset-sum/
# 输入: [1, 5, 11, 5]
# 输出: true
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 分析：
# dp[4][9] = true，其含义为：对于容量为 9 的背包，若只是用前 4 个物品，可以有一种方法把背包恰好装满。
# 容量是sum/2
# 思路是遍历这个数组，每到一个位置判断有多少种方法得到结果
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2 == 1:
            return 0

        half_sum = total_sum // 2
        dp = [[0] * (half_sum + 1) for i in range(n)]  # todo 为啥n不用+1？？
        if nums[0] <= half_sum:
            dp[0][nums[0]] = 1

        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(half_sum + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
            if dp[i][-1] == 1:
                return True
        return dp[-1][-1]

    def canPartition1(self, nums):
        """
        dp[i][j],i是使用前i+1个数，j是需要组成的和??todo
        :param nums:
        :return:
        """
        l = len(nums)
        sum_n = sum(nums)
        if sum_n % 2 != 0:
            return 0
        sum_2 = sum_n / 2
        dp = [[0 for j in range(sum_2 + 1)] for j in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(1, sum_2 + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
        return dp[l + 1][sum_2]

    # todo 只用一维数组记录可以吗？
    def canPartition2(self, nums):
        nums_sum = sum(nums)
        l_nums = len(nums)
        if nums_sum & 1 == 1:
            return 0
        half_nums = nums_sum // 2

        dp = [[0] * (half_nums + 1) for _ in range(l_nums )]
        for i in range(l_nums):
            for j in range(1, half_nums + 1):
                # dp[i][j]=dp[i-1][j]
                dp[i][j] = dp[i - 1][j]  # 这一步很重要很重要！！！
                print(i, nums[i], j)
                if nums[i] == j:  # 只需要nums[i-1]一个数就可以得到j
                    dp[i][j] = 1
                elif nums[i] < j:  # nums[i-1]<j时，和前面的数加起来是j,或者前面的数的和已经成为了j
                    # print(i,j,dp[i - 1][j],dp[i-1][j-nums[i-1]])
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                if dp[i][half_nums]:
                    print(i,half_nums)
                    return 1
        print(dp)
        return dp[-1][-1]
    # todo 只用一维数组记录可以吗？

    def canPartition2g(self, nums):
        nums_sum = sum(nums)
        l_nums = len(nums)
        if nums_sum & 1 == 1:
            return False
        half_nums = nums_sum // 2

        dp = [False for _ in range(half_nums + 1)]
        for i in range(l_nums):
            for j in range(half_nums, 0, -1):
                # dp[i][j]=dp[i-1][j]
                if nums[i] == j:  # 只需要nums[i-1]一个数就可以得到j
                    # print(i, nums[i], j, dp)
                    dp[j] = True
                elif nums[i] < j:  # nums[i-1]<j时，和前面的数加起来是j,或者前面的数的和已经成为了j
                    # print(i,j,dp[i - 1][j],dp[i-1][j-nums[i-1]])
                    # print(i, nums[i], j, dp)
                    dp[j] = dp[j] or dp[j - nums[i]]
                # if dp[half_nums]:
                #     print(i,half_nums, dp)
                #     return 1
                # print(i, nums[i], j, dp)
        return dp[-1]


if __name__ == '__main__':
    # print(Solution().canPartition2([1, 5, 11, 5]))
    # print(Solution().canPartition([1, 5, 11, 5]))
    # print(Solution().canPartition2([1, 3, 4, 4]))
    # print(Solution().canPartition([1, 3, 4, 4]))
    # print(Solution().canPartition2([2, 2, 1, 1]))
    # print(Solution().canPartition2([1,2,3,5]))
    print(Solution().canPartition2([1,5,10,6]))
    # print(Solution().canPartition2([1,2,5]))
    # print(Solution().canPartition2([2,2,3,5]))
