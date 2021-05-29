class Solution:
    def findTargetSumWays(self, nums, S):
        l = len(nums)
        sum_nums = sum(nums)
        all_sum_nums = 2 * sum(nums) + 1
        # dp=[for _ in range(l) r]
        # for
        # dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]  # dp[i][j]代表前i个数，结果为j的可能性个数

    def findTargetSumWays1(self, nums, S):

        sumAll = sum(nums)
        if S > sumAll or (S + sumAll) % 2:
            return 0
        target = (S + sumAll) // 2  # 相加的个数

        dp = [0] * (target + 1)
        dp[0] = 1
        # 遍历nums,每遍历到一个数num，如果有dp[j-num],则会有dp[j-num]+dp[j]=dp[j]
        for num in nums:  # 遍历nums
            for j in range(target, num - 1, -1):  # 当遍历到数字num时，倒着遍历target到num-1  todo 倒着遍历的的目的是：最先得到的是大数的dp值
                dp[j] = dp[j] + dp[j - num]  # dp[j]表示，nums中和为j的情况数，
                # 当前填满容量为j的包的方法数 = 之前填满容量为j的方法数 + 之前填满容量为（j - num）的方法数
            print(dp)
        return dp[-1]

    def findTargetSumWays2(self, nums, S):
        l_sum = sum(nums)
        if l_sum < S or (l_sum + S) % 2:
            return 0
        add_sum = (l_sum + S) // 2  # 相加的1的个数
        dp = [0] * (add_sum + 1)
        dp[0] = 1  #！！！
        for num in nums:
            #     dp[num]=1
            for i in range(add_sum, num - 1, -1):
                dp[i] = dp[i - num] + dp[i]
        return dp[-1]

    def findTargetSumWays3(self, nums, S):
        """
        参考https://leetcode-cn.com/problems/target-sum/solution/494-mu-biao-he-dong-tai-gui-hua-zhi-01be-78ll/ 写了个二维的
        """
        l_sum = sum(nums)
        if l_sum < S or (l_sum + S) % 2:
            return 0
        add_sum = (l_sum + S) // 2  # 相加的1的个数
        l_len = len(nums)
        if l_len<2 and abs(l_sum)==abs(S):  # todo 为什么一维的要单独处理
            return 1
        elif l_len<2 and abs(l_sum)==abs(S):
            return 0
        print("l_len--",l_len,"add_sum + 1--",add_sum + 1)
        dp = [[0 for i in range(l_len)] for _ in range(add_sum + 1)]
        dp[0][0]=1
        dp[0][nums[0]]=1
        for i in range(1,l_len):
            for j in range(add_sum, nums[i] - 1, -1):
                print(i,j,i-1,j - nums[i])
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
            print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    # print(s.findTargetSumWays3(nums= [1, 1, 1, 1, 1], S=3))
    print(s.findTargetSumWays3(nums= [0,0,0,0,0,0,0,0,1], S=1))
    print("-----")
    # print(s.findTargetSumWays2(nums=[1, 1, 1, 1, 1], S=3))
