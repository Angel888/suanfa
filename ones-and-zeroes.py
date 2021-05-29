# https://leetcode-cn.com/problems/ones-and-zeroes/
# 示例 1:
#
# 输入: strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出: 4
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
# 示例 2:
#
# 输入: strs = ["10", "0", "1"], m = 1, n = 1
# 输出: 2
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
#  
# 相似的动态规划：
# partition-equal-subset-sum.py
# beibao.py

# dp(i, j) = max(1 + dp(i - cost_zero[k], j - cost_one[k])) if i >= cost_zero[k] and j >= cost_one[k]
# 比较拼这个数和不拼这个数哪个更大
c=[
[[0, 0],
 [0, 0]
 ],

[[0, 0], [0, 0]],
[[0, 0], [0, 0]],
[[0, 0], [0, 0]]
]
class Solution:
    def findMaxForm(self, strs, m: int, n: int):
        if len(strs) == 0:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for strs_item in strs:  # 遍历每一个字符串  todo  判断先放哪个字符串的个数多？？
            item_count0 = strs_item.count('0')  # 一共有多少个'0'
            item_count1 = strs_item.count('1')

            # 遍历可容纳的背包  item_count0 - 1的原因是到-1是遍历到0
            for i in range(m, item_count0 - 1, -1):  # 采取倒序  # todo 为什么要采用倒叙？？
                for j in range(n, item_count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - item_count0][j - item_count1])
                    print(i, j, dp[i][j])
                    # max是判断该字符串放与不放，  todo 为什么dp的行和列都比m,n大1？为什么i和j每个字符都会填充？
            print(dp)

        return dp[m][n]

    def findMaxForm1(self, strs, m: int, n: int):  # m个0，n个1
        l=len(strs)
        # dp=[[0 for i in range(2)] for i in range(2)]
        dp=[[[0]*(n+1) for _ in range(m+1)]for __ in range(l+1)]  # todo 三维数组
        # print(dp)
        for a in range(1,l+1):
            z_o = self.get_zero_num(strs[a-1])
            z_n=z_o[0]
            o_n=z_o[1]
            for j in range(m+1): # 字符0
                for i in range(n+1):  # 字符1
                    # print('z_n，o_n----', o_n, z_n)
                    # print("dp[a][j][i],dp[a-1][j-z_n][i-o_n]----",dp[a][j][i],dp[a-1][j-z_n][i-o_n])
                    if z_n<=j and o_n <=i:
                        dp[a][j][i]=max(dp[a-1][j-z_n][i-o_n]+1,dp[a-1][j][i])  # todo 是否存在要先取出来一个字符串，才能放这个字符穿的情况，怎么处理？
                        dp[a][j][i]=dp[a-1][j][i]
        # print('~~~dp[2][1][1]',dp[2][1][1])  # m=1,n=1时，放到第2个字符串时，可以放1个
        # print('~~~dp[3][1][1]',dp[3][1][1])
        print("!!!",dp[-1][-1][-1])
        return dp[-1][-1][-1]


    def get_zero_num(self,strs):
        z_o=[]
        z=0
        o=0
        for i in strs:
            if ord(i)-ord("0")==1:
                o+=1
            else:
                z+=1
        z_o.append(z)
        z_o.append(o)
        return z_o


if __name__ == '__main__':
    # Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
    # Solution().findMaxForm1(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
    # Solution().findMaxForm1(strs=["10","0","1"], m=1, n=1)
    Solution().findMaxForm1(strs=["10","0001","111001","1","0"], m=4, n=3)
