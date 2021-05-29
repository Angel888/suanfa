# https://leetcode-cn.com/problems/


class Solution:
    def numSquares(self, n: int):
        """
        从1开始遍历每个数。
        当遍历到底i个数时，从1开始遍历，直到i
        :param n:
        :return:
        """
        dp = []
        dp.append(0)
        for i in range(1,n + 1):
            j = 1
            dp.append(i)
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        # print(dp)
        return dp[-1]

    def debug(func):
        def wrapper(self, *args, **kwargs):
            print("[DEBUG]: enter {}()".format(func.__name__))
            return func(self, *args, **kwargs)
        return wrapper

    @debug
    def numSquares1(self, n: int) -> int:

        # from collections import deque
        # deq = deque()
        # visited = set()
        #
        # deq.append((n, 0))
        # while deq:
        #     number, step = deq.popleft()
        #     targets = [number - i * i for i in range(1, int(number ** 0.5) + 1)]
        #     for target in targets:
        #         if target == 0: return step + 1
        #         if target not in visited:
        #             deq.append((target, step + 1))
        #             visited.add(target)
        return 0

def aaa():
    return 'aaaaaa'

if __name__ == '__main__':
    s = Solution()
    s.numSquares1(12)
