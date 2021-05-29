class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        res = [1]
        for i in range(1, l):
            if s[i] != s[i - 1]:
                res.append(res[i - 1] + 1)
            else:
                res.append(1)
        return max(res)

    def lengthOfLongestSubstring1(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # 获取索引 i  dic词典记录的是某个字符最近出现的位置
            dic[s[j]] = j  # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # max(dp[j - 1], dp[j])
        return res

    def lengthOfLongestSubstring2(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)  # 更新左指针 i
            dic[s[j]] = j  # 哈希表记录
            res = max(res, j - i)  # 更新结果
        return res


    def lengthOfLongestSubstring3(self, s: str) -> int:
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i -= 1 # 线性查找 i  每次查找离该字符最近的字符
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]  tmp为上个字符的位置的最大的不含重复字符的长度
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res
    # def longest(self,s):
    #     l=len(s)
    #     for i in s:
    def lengthOfLongestSubstring4(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res

    def lengthOfLongestSubstring5(self, s: str) -> int:
        if s==" ":
            return 1
        head,tmp=0,0
        l=len(s)
        m={}
        for i in range(l):
            if s[i] in m:
                head=max(head,m[s[i]])
            m[s[i]]=i+1
            tmp=max(tmp,i-head+1)
        return tmp



if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring5("abcabcbb"))
    print(s.lengthOfLongestSubstring5("a"))
