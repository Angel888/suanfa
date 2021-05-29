# dp[3][5] = 6，其含义为：对于给定的一系列物品中，若只对前 3 个物品进行选择，当背包容量为 5 时，最多可以装下的价值为 6。
# dp是把5装满可以装的最大价值！！！
# dp[i][w] = max(dp[i-1][w],dp[i-1][w - wt[i-1]] + val[i-1])   !!!!w的值是还没放i物品的体积！！！
# dp[i-1][w] 代表不装；也就是此时包的容量为w，已经装了i-1件物品时，还能够装的最大价值
# dp[i-1][w - wt[i-1]] + val[i-1]代表装。当前包的容量为（w - wt[i-1]），已经装了i件物品时，还能够装的最大价值
#
# https://mp.weixin.qq.com/s/RXfnhSpVBmVneQjDSUSAVQ
class Solution:
    # def classic_beibao(self, n, w, w_l, v_l):  # w表示总重量,n表示物品的件数，w_l是列表,v_l是列表，表示每件物品的价值
    #     dp = [[0 for __in in range(w+1)] for _ in range(n+1)]
    #     # 思路就是装每一件物品时，判断每个w下还能装的最大价值？？
    #     for i in range(1,n+1):  # todo 为啥从1开始算？
    #         for j in range(1,w - w_l[i-1]+1):  # 在已经装了那件i物品的情况下
    #             if j - w_l[i-1] < 0:
    #                 dp[i][j] = dp[i - 1][j]
    #             else:
    #                 dp[i][j] = max(dp[i - 1][j - w_l[i - 1]] + v_l[i - 1],
    #                                dp[i - 1][j])
    #     return dp[n][w]  # todo 为什么return的是n和w??
    def pack1(self,w, v, C):  # 每个东西只能选择一次
        dp = [[0 for _ in range(C + 1)] for _ in range(len(w) + 1)]
        for i in range(1, len(w) + 1):  # w是物体的列表
            for j in range(1, C + 1):   # j代表当前的剩余容量
                if j < w[i - 1]:  # 如果剩余容量不够新来的物体 直接等于之前的
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
        print(dp)
        return dp[len(w)][C]


if __name__ == '__main__':
    # print(Solution().classic_beibao(n=3, w=4, w_l=[2, 1, 3], v_l=[4, 2, 3]))
    # print(Solution().pack1(w=[2, 3, 4, 5], v=[3, 4, 5, 6], C=8))
    print(Solution().pack1(w=[2, 1, 3], v=[4, 2, 3], C=4))
