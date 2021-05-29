# https://leetcode-cn.com/problems/number-of-islands/
# 1代表陆地
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
from nltk import collections
#  深度优先用的是递归，广度优先用的是队列
class Solution:

    def dfs(self, grid, r, c):
        grid[r][c] = 0  # 已经遍历过的标记为0！！！
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # 四个方向
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands1(self, grid) -> int:
        """
        最终岛屿的数量就是我们进行深度优先搜索的次数
        :param grid:
        :return:
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):  # 从左到右，每个1格子深度遍历
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)
        print("num_islands---", num_islands)
        return num_islands

    def numIslands2(self, grid) -> int:
        """
        使用双边队列作为队列
        :param grid:
        :return:
        """

        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

    def numIslands3(self, grid) -> int:

        def dfs1(i, j):
                grid[i][j]=0
                for d in directions:
                    m=i + d[0]
                    n=j + d[1]
                    if 0 <= m < a and 0 <= n < b and grid[m][n] == "1":
                        dfs1(m,n)
        res = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        a = len(grid)
        if a==0:
            return 0
        b = len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j] == "1":
                    res += 1
                    dfs1(i, j)
        # print("~~~~", res)
        return res


if __name__ == '__main__':
    # Solution().numIslands1(
    #     [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
    Solution().numIslands3(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
