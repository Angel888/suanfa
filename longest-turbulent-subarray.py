# https://leetcode-cn.com/problems/longest-turbulent-subarray/
# 动态规划
from filecmp import cmp
from xlwings import xrange


# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
#
class Solution(object):
    # def maxTurbulenceSize(self, A):
    #     N = len(A)
    #     ans = 1
    #     anchor = 0
    #
    #     for i in xrange(1, N):
    #         c = cmp(A[i - 1], A[i])   # 比较i-1和i的大小,结果为1，-1，0
    #         if i == N - 1 or c * cmp(A[i], A[i + 1]) != -1: #
    #             if c != 0:
    #                 ans = max(ans, i - anchor + 1)
    #             anchor = i
    #     print(ans)
    #     return ans
    def maxTurbulenceSize(self, A):
        N = len(A)
        if N < 2:
            return N
        a = [0 for i in range(N)]
        a[0] = 1
        if A[1] == A[0]:
            a[1] = 1
        else:
            a[1] = 2
        if N > 1:
            for p in range(2, N):
                if A[p] > A[p - 1] and A[p - 2] >= A[p - 1]:
                    a[p] = a[p - 1] + 1
                elif A[p] < A[p - 1] and A[p - 2] <= A[p - 1]:  # 2>1
                    a[p] = a[p - 1] + 1
                elif A[p] == A[p - 1]:
                    a[p] = 1
                elif A[p] > A[p - 1] > A[p - 2]:
                    a[p]=2
                elif A[p] < A[p - 1] < A[p - 2]:
                    a[p]=2

        res = max(a)
        return res


if __name__ == '__main__':
    Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
    # Solution().maxTurbulenceSize([4,8,12,16])
    # Solution().maxTurbulenceSize([100])
    # Solution().maxTurbulenceSize([9,9])
    # Solution().maxTurbulenceSize([0,1,1,0,1,0,1,1,0,0])
    # Solution().maxTurbulenceSize([0,1,1,0,1,0,1,1,0,0])
    # Solution().maxTurbulenceSize([8, 8, 9, 10, 6, 8, 2, 4, 2, 2, 10, 6,
    #                               6, 10, 10, 2, 3, 5, 1, 2, 10, 4, 2, 0, 9, 4, 9, 3, 0, 6, 3, 2, 3,
    #                               10, 10, 6, 4, 6, 4, 4, 2, 5, 1, 4, 1, 1, 9, 8, 9, 5, 3, 5, 5, 4, 5,
    #                               5, 6, 5, 3, 3, 7, 2, 0, 10, 9, 7, 7, 3, 5, 1, 0, 9, 6, 3, 1, 3, 4, 4, 3, 6, 3, 2,
    #                               1, 4, 10, 2, 3, 4, 4, 3, 6, 7, 6, 2, 1, 7, 0, 6, 8, 10])
