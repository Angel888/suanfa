# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/  #todo 下次没有思路时，可以先使用for，然后再改成递归
class Solution:
    def permutation(self, s: str):
        c, res = list(s), []  # 字符串转换为列表

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # c是每次拼接成的列表
                return
            dic = set()  # todo dic里面保存的是什么？怎样排除重复的字符？
            for i in range(x, len(c)):
                if c[i] in dic: continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res

    def permutation1(self, s: str):
        l = len(s)
        c = list(s)

        def dfs(x):
            t = set()
            for j in range(x, l):
                if s in t: continue
                c[j], c[x] = c[x], c[j]
                dfs(x+1)
                dfs()
