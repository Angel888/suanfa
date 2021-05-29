# https://leetcode-cn.com/problems/number-of-islands/
import collections


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: [[]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        # nr是竖，nc是横
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":  # 1是陆地
                    num_islands += 1
                    self.dfs(grid, r, c)  # r，c是坐标

        return num_islands

    def numIslands1(self, grid: [[]]):
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
                    neighbors = collections.deque([(r, c)])  # 创建一个名为neighbor的双边队列，可以解决约瑟夫问题
                    # 大概意思就是每个为1的点绕四周找一下  todo  这也算BFS  ????
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:  # 四个方向遍历
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":  # 如果是1，则加入到neighbors双边队列中
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

    from typing import List
    # 使用并查集


# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
#

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)  # 长度为20的list
        self.rank = [0] * (m * n)  # 长度为0的list
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j       # parent标记为1的位置
                    self.count += 1    # 值为1的点的个数

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution3:
    def numIslands3(self, grid: [[]]):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"  # 把为1的点变成0
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)  # todo 啥意思？？？

        return uf.getCount()








if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
