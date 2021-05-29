# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
class Solution:
    def maxProfit(self, prices):
        l = len(prices)
        r = [[0] * (l + 1) for _ in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(i, l + 1):
                a = prices[j] - prices[i]

    def maxProfit1(self, prices) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

    def maxProfit2(self, prices):
        l=len(prices)
        cost,profit=prices[0],0
        for i in range(l):
            profit=max(profit,prices[i]-cost)
            cost=min(cost,prices[i])
        return profit
if __name__ == '__main__':
    s=Solution()
    print(s.maxProfit2([7,1,5,3,6,4]))
