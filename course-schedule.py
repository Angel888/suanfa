# 你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#  
#
# 提示：
#
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
#
# 链接：https://leetcode-cn.com/problems/course-schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]  # 构建长度为numCourses的列表adjacency，每一项为[]
        flags = [0 for _ in range(numCourses)]  # 构建长度为numCourses的列表flags，每一项为0
        for cur, pre in prerequisites:  # 遍历prerequisites，将
            adjacency[pre].append(cur)
            print(adjacency)
        for i in range(numCourses):  # todo adjacency有什么用？
            if not dfs(i, adjacency, flags): return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
