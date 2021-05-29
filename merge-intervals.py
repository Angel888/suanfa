# https://leetcode-cn.com/problems/merge-intervals/  #todo
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并 为 [1,6].
#
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
class Solution:
    # def merge(self, intervals):
    #     intervals.sort(key=lambda x: x[0])
    #
    #     merged = []
    #     for interval in intervals:
    #         # 如果列表为空，或者当前区间与上一区间不重合，直接添加
    #         if not merged or merged[-1][1] < interval[0]:
    #             merged.append(interval)
    #         else:
    #             # 否则的话，我们就可以与上一区间进行合并
    #             merged[-1][1] = max(merged[-1][1], interval[1])
    #
    #     return merged
    def merge(self, intervals):
        """
        1 先对区间排序  区间本来就是有序的吗?如果不是，则先按照lambda的方式排序  todo 如果是用java，怎么排呢？
        2 判断每个区间是否与上一个有包含关系
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print("intervals~~~~",intervals)
        a = len(intervals) - 1
        i = 0
        while i < a:
            # for i in range(a-1):
            if intervals[i + 1][0] <= intervals[i][1] :  # i+1被包含
                intervals[i]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
                intervals.pop(i + 1)
                a -= 1
            else:
                i += 1
        print(intervals)
        return intervals


if __name__ == '__main__':
    # Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    # Solution().merge([[1,4],[4,5]])
    # Solution().merge([[1,4],[0,0]])  # [[0,0],[1,4]]
    Solution().merge([[1,4],[0,2],[3,5]])  # [[0,5]]
