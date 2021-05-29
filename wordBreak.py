class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        # dp[i] 表示 ss 的前 i 位是否可以用DictwordDict 中的单词表示。
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, n + 1):
                    # print(dp)
                    if s[i:j] in wordDict:  # 如果i到j可以用单词表示，前i位也可以用单词表示，那么dp[j]为true
                        dp[j] = True
        # print(dp[-1])
        return dp[-1]

    def wordBreak1(self, s: str, wordDict) :



if __name__ == '__main__':
    s = Solution()
    s.wordBreak(s="leetcode", wordDict=["leet", "code"])
