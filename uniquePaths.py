# https://leetcode-cn.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print("dp-----", dp)
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                print(i, "~", j, "\n")
                print("dp[i-1][j]------", dp[i - 1][j], "\ndp[i][j-1]", dp[i][j - 1], "\n")
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                print(dp[i][j], "\n")
        return dp[-1][-1]

    def uniquePaths1(self, m: int, n: int) -> int:  # 这个方法相比于上一个，每次只保存一行数，用的是一维数组，所以时间复杂度很小
        pre = [1] * m
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                print(i, "~", j, "\n")
                print('pre[j]----', pre[j], "cur[j - 1]---", cur[j - 1])
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
            print("pre~~~", pre)
        return pre[-1]

    def uniquePaths2(self, m: int, n: int) -> int:   #这个方法是直接在之前数组的基础上改
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):

                cur[j] += cur[j - 1]
        print(cur)
        return cur[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths2(7, 3))
