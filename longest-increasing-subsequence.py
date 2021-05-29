# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 每次都要遍历一下前面的，只需要一个列表记录本次最大的值
# todo 自己做一遍
class Solution:
    def lengthOfLIS(self, nums):
        # 这个二分法没看懂https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res


if __name__ == '__main__':
    Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
