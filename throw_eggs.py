# https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E9%AB%98%E6%A5%BC%E6%89%94%E9%B8%A1%E8%9B%8B%E9%97%AE%E9%A2%98.md
# N层楼，K个鸡蛋  最坏情况下，你至少要扔几次鸡蛋，才能确定会摔坏的楼层 todo
class Solution:
    def superEggDrop(K: int, N: int):
        memo = dict()

        def dp(K, N) -> int:
            # base case
            if K == 1: return N   # 最高层摔坏
            if N == 0: return 0   # 不需要扔
            # 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 穷举所有可能的选择
            for i in range(1, N + 1):
                res = min(res,
                          max(
                              dp(K, N - i),
                              dp(K - 1, i - 1)
                          ) + 1
                          )
            # 记入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)
