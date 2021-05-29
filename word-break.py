# https://leetcode-cn.com/problems/word-break/   #todo again
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。


class Solution:


    def wordBreak1(self, s: str, wordDict) -> bool:
        import functools
        @functools.lru_cache(3)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res
        a=back_track(s)
        print("1",a)
        return a

    def wordBreak2(self, s: str, wordDict) -> bool:
        # dp[i]表示第i个是否可以被表示
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):  # 遍历字符串
            for j in range(i + 1, n + 1):  # 遍历i+1到n+1的部分
                if (dp[i] and (s[i:j] in wordDict)):  # todo s[i:j] in wordDict 怎么判断？
                    dp[j] = True
        return dp[-1]

    def wordBreak3(self, s: str, wordDict) -> bool:
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(l):  # todo 这里为什么是l而不是l+1？  因为要遍历l次
            for j in range(i + 1, l + 1):
                if dp[i] == True and s[i:j] in wordDict:
                    dp[j] = True
        print(dp[-1])
        return dp[-1]


if __name__ == '__main__':
    Solution().wordBreak1(s="applepenapple", wordDict=["apple", "pen"])  # len(s)=13
    Solution().wordBreak3(s="applepenapple", wordDict=["apple", "pen"])
