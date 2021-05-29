# https://blog.csdn.net/qq_22526061/article/details/83504116  背包的python
# n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？
#
# 为方便讲解和理解，下面讲述的例子均先用具体的数字代入，即：eg：number＝4，capacity＝8
# w代表体积，v代表价值()
# number＝4，capacity＝8
goods = [(2, 3), (3, 4), (4, 5), (5, 6)]  # 第0位是体积，第1位是价值
capacity = 8


def O_1_backpack(goods, capacity):
    """F [i, v] 表示前 i 件物品恰放入一个容量为 v 的背包可以获得 的最大价值。f[0][v】都是0"""
    g_l = len(goods)
    # dp = [[0 for i in range(capacity + 1)] for j in range(g_l + 1)]  # todo 为什么capacity是内层的列表
    dp = [[0]* (capacity + 1) for j in range(g_l + 1)]  # todo 为什么capacity是内层的列表  我的理解是要先把容量为i的最大价值找出来，然后找容量为i+1的最大价值
    print("capacity+1---", capacity + 1, "g_l+1---", g_l + 1)
    for i in range(1, g_l + 1):  # 物品个数  #todo 一定要注意边界为0的dp结果是0，
        for j in range(1, capacity + 1):  # 容量
            print("i,j---", i, j)
            # print(dp[i-1][j],dp[i-1][j-goods[i][0]],goods[i][1])
            if j >= goods[i - 1][0]:   # 一定要注意这个判断是>=0
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - goods[i - 1][0]] + goods[i - 1][1])  # todo 这里一定要注意是goods是（i-1）
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    print(dp[-1][-1])
    # 最终的结果应该是10 ！！！
    return dp[-1][-1]

# 完全背包问题
# 和01背包的区别是每个物品都有无限件
# 每件物品的价值是v，重量是w，可以放无限件，则同样的空间，一个物品的价值是w/v，则可以知道每个物品的单位价值，先放单位价值最大的。
# 首先将费用大于 V 的物品去掉，然后用计数排序，计算价值最高的那个
if __name__ == '__main__':
    O_1_backpack(goods, capacity)
