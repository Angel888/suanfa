# https://leetcode-cn.com/problems/maximum-width-ramp/ todo python的__getitem__，bisect看不懂

# 输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
#
# 输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
import bisect

from xlwings import xrange


class Solution:
    def maxWidthRamp(self, A):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key=A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
    def maxWidthRamp1(self, A):
        N = len(A)

        ans = 0
        candidates = [(A[N-1], N-1)]
        # candidates: i's decreasing, by increasing value of A[i]
        for i in xrange(N-2, -1, -1):
            # Find largest j in candidates with A[j] >= A[i]
            jx = bisect.bisect(candidates, (A[i],))
            if jx < len(candidates):
                ans = max(ans, candidates[jx][1] - i)
            else:
                candidates.append((A[i], i))

        return ans

for i in sorted(range(len([6,0,8,2,1,5])), key=[6,0,8,2,1,5].__getitem__):
    print(i)