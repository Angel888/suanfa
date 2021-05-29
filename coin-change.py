# https://leetcode-cn.com/problems/coin-change/  todo
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。x
import sys
#dp相关的题
#todo 用dp再做一遍 https://leetcode-cn.com/problems/coin-change/solution/javadi-gui-ji-yi-hua-sou-suo-dong-tai-gui-hua-by-s/
#todo https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    # def change(self, amount: int, coins) :
    #     coins=sorted(coins)
    #     res=[]
    #     def get_one_coin(amount,coins):
    #         for i in coins:
    #             if i>amount:
    #                 continue
    #             elif i==amount:
    #                 return
    #             else:
    #
    #                 get_one_coin(amount-i,coins[:i+1])
    #     get_one_coin(amount,coins)
    def coinChange(self, coins, amount: int) -> int:
        coins.sort(reverse=True)
        l = len(coins)
        print(coins)
        i = 0
        res = 0
        while amount > 0:
            print(amount, coins[i])
            shang = amount // coins[i]
            if shang >= 1:
                res += amount // coins[i]
                amount = amount % coins[i]
            i += 1
            if i == l and amount > 0:
                return -1
        print("res--", res)
        return res

    def coinChange1(self, coins, amount: int) -> int:
        """
        仿写c++答案https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/
        """
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        self.ans = sys.maxsize
        self.get_ans(coins, amount, 0, 0)
        # print(self.ans)
        if self.ans == sys.maxsize:
            return -1
        return self.ans

    def get_ans(self, coins, amount, c_index, count):
        if amount == 0:
            self.ans = min(self.ans, count)
            return
        if c_index == len(coins):  # todo 素有的硬币已经遍历完了
            return
        k = amount // coins[c_index]
        while k >= 0 and k + count < self.ans:
            self.get_ans(coins, amount - k * coins[c_index], c_index + 1, count + k)
            k -= 1



if __name__ == '__main__':
    s = Solution()
    s.coinChange([1, 2, 5], 11)
    s.coinChange1([1, 2, 5], 11)
    s.coinChange1([186, 419, 83, 408], 6249)
