# https://leetcode-cn.com/problems/longest-common-subsequence/   #todo 使用动态规划和纯粹的递归时间复杂度相差有多少？？
# 最长公共子序列
class Solution:
    def longestCommonSubsequence(self, str1, str2) -> int:
        """
        最原始的递归
        :param str1:
        :param str2:
        :return:
        """

        def dp(i, j):
            # 空串的 base case
            if i == -1 or j == -1:  # 递归结束的地方
                return 0
            if str1[i] == str2[j]:
                # print("!")
                # 这边找到一个 lcs 的元素，继续往前找  todo 为啥往前找？
                return dp(i - 1, j - 1) + 1
            else:
                # 谁能让 lcs 最长，就听谁的
                return max(dp(i - 1, j), dp(i, j - 1))

        a = dp(len(str1) - 1, len(str2) - 1)
        return a

    def longestCommonSubsequence2(self, str1, str2):
        # i 和 j 初始化为最后一个索引
        a = len(str1)
        b = len(str2)

        def dp1(i, j):
            if i < a and j < b:
                if str1[i] == str2[j]:
                    return dp1(i + 1, j + 1) + 1

                else:
                    return max(dp1(i, j + 1), dp1(i + 1, j))
            else:
                return 0

        a = dp1(0, 0)
        print("a", a)
        return a

    def longestCommonSubsequence1(self, str1, str2) -> int:
        """
        通过备忘录优化了时间复杂度的dp  todo 有了dp这个表和单纯的递归有啥区别？
        :param str1:
        :param str2:
        :return:
        """
        m, n = len(str1), len(str2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        # dp[i][j]代表的是每个i和j时最大的值
        for i in range(1, m + 1):  # todo 为啥要m+1?
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print("longestCommonSubsequence1,",dp[-1][-1])

        return dp[-1][-1]

    def longestCommonSubsequence3(self, str1, str2):
        a = len(str1)
        b = len(str2)
        # dp = [[0] * (b + 1)] * (a + 1)
        dp = [[0] * (b + 1) for _ in range(a + 1)]
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  # todo 很重要！！！
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print("-----", dp[a][b])
        return dp[a][b]


if __name__ == '__main__':
    # Solution().longestCommonSubxsequence2("pmjghexybyrgzczy","hafcdqbgncrcbihkd")
    # Solution().longestCommonSubsequence3("pmjghexybyrgzczy","hafcdqbgncrcbihkd")
    Solution().longestCommonSubsequence1("abcde", "ace")
    Solution().longestCommonSubsequence3("abcde", "ace")
    Solution().longestCommonSubsequence1("abcba", "abcbcba")
    Solution().longestCommonSubsequence3("abcba", "abcbcba")
