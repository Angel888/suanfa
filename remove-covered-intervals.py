# https://leetcode-cn.com/problems/remove-covered-intervals/
# 删除被其他区间覆盖的区间，你返回列表中剩余区间的数目。
# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
"""
也就是说，这种区间问题的解法
首先，如果是两个元素，则先看左区间是否比另一个元素小；左区间相同的话，则看右区间有没有在外面。
找包含就是看左边的是否大，右边的是否小；然后按照这种包含的关系重新排列列表，这样更容易看出每个元素和它周围元素的包含关系
"""


class Solution:
    def removeCoveredIntervals(self, intervals):
        """
        首先将所有元素先按照第一个元素排列，如果第一个元素相同，则按照第二个元素倒序排列。
        排列后的列表，如果第二个元素无法大于前面存在的第二个元素，则舍弃
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))  # todo 为什么这样写就是先按照第一个排序，然后按照第二个逆序？？？
        # g = lambda x: (x[0], -x[1])
        # print("intervals~~~~~1", g([1, 4]))  # (1, -4)
        # print("intervals~~~~~2", g([3, 6]))  # (3, -6)
        # print("intervals~~~~~3", g([2, 8]))  # (2, -8)
        count = 0
        # print("11！", intervals)  # [[1, 4], [2, 8], [3, 6]]
        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            # print("_, end~~~~~~",_, end)
            # print("end , prev_end~~~~~",end , prev_end)
            if end > prev_end:
                count += 1
                prev_end = end
        print(count)
        return count

    # alist  =  [( '2' ,  '3' ,  '10' ), ( '1' ,  '2' ,  '3' ), ( '5' ,  '6' ,  '7' ), ( '2' ,  '5' ,  '10' ), ( '2' ,  '4' ,  '10' )]
    # # 多级排序，先按照第3个元素排序，然后按照第2个元素排序：
    # print(sorted (alist,  cmp  =  None , key  =  lambda  x:( int (x[ 2 ]),  int (x[ 1 ])), reverse  =  False ))
    def removeCoveredIntervals1(self, intervals):
        """
        前面和后面是包含与被包含关系
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        a = len(intervals)
        c = 0
        tmp=intervals[0]
        for j in range(a - 1):
            i = j + 1
            if tmp[0] <= intervals[i][0] and tmp[1] >= intervals[i][1]:
                c += 1
            else:
                tmp=intervals[i]
        d = a - c
        # print(d)
        return d


if __name__ == '__main__':
    Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8],[2,6]])
    Solution().removeCoveredIntervals1([[1, 4], [3, 6], [2, 8],[2,6]])
    Solution().removeCoveredIntervals([[1, 3], [2, 4], [3, 6]])
    Solution().removeCoveredIntervals1([[1, 3], [2, 4], [3, 6]])
    Solution().removeCoveredIntervals([[0, 10], [5, 12]])
    Solution().removeCoveredIntervals1([[0, 10], [5, 12]])
    Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]])
    Solution().removeCoveredIntervals1([[1,2],[1,4],[3,4]])
