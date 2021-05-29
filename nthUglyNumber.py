# https://leetcode-cn.com/problems/chou-shu-lcof/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            # print(i, n2, n3, n5)
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1  # todo  这一步会用到已经获取的值，没想到
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]

    def nthUglyNumber1(self, n):
        res = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            r_a = res[a] * 2
            r_b = res[b] * 3
            r_c = res[c] * 5
            print(i,r_a, r_b, r_c)
            m = min(r_a, r_b, r_c)
            res[i]=m
            if res[i] == r_a:
                a += 1
            if res[i] == r_b:
                b += 1
            if res[i] == r_c:
                c += 1
        return res[-1]


if __name__ == '__main__':
    Solution().nthUglyNumber(10)
    Solution().nthUglyNumber1(10)
