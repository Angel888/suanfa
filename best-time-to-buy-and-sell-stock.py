# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# todo  不用dp数组，自己做一遍

class Solution:
    def maxProfit(self, prices):
        """计算每次 到当天为止 的最小股票价格和最大利润"""
        minprice = float('inf')
        maxprofit = 0
        for price in prices:  # 遍历price
            minprice = min(minprice, price)  # prince  每次都找一个尽量小的数，作为买进
            maxprofit = max(maxprofit, price - minprice)  # 每次都减去当前最小的数，并和之前的maxprofit比较，最终获得最大的差！！！
        return maxprofit


# dp[i]=max(dp[i−1],prices[i]−minprice)   dp中的每个元素代表到那一天的最大利润
class Solution1:
    def maxProfit1(self, prices):
        n = len(prices)
        if n == 0: return 0  # 边界条件
        minprice = prices[0]
        dp = [0] * n
        dp[0] = 0
        for i in range(1, n):
            minprice =min(minprice,prices[i])
            dp[i] = max(dp[i-1], prices[i] - minprice)
        return dp[-1]

