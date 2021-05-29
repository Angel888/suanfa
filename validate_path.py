# https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid/
from _ast import List


class Solution:
    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        ds = Solution.DisjointSet(n * m)

        def getId(x, y):
            return x * m + y

        def detectL(x, y):   # 左边的必须是1，4，6
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        def detectR(x, y):
            if y + 1 < m and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        def detectD(x, y):
            if x + 1 < n and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        def handler(x, y):
            if grid[x][y] == 1:   # 如果只有一个格子
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:
                detectL(x, y)
                detectU(x, y)
            else:
                detectR(x, y)
                detectU(x, y)

        for i in range(n):
            for j in range(m):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(n - 1, m - 1))


class Solution1:
    class DisjointSet:
        def __init__(self, n):
            self.f = list(range(n))

        def find(self, x):
            if x == self.f[x]:
                return x
            self.f[x] = self.find(self.f[x])
            return self.f[x]

        def merge(self, x, y):
            self.f[self.find(x)] = self.find(y)

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        patterns = [0, 0b1010, 0b0101, 0b1100, 0b0110, 0b1001, 0b0011]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ds = Solution1.DisjointSet(n * m)

        def getId(x, y):
            return x * m + y

        def handler(x, y):
            pattern = patterns[grid[x][y]]
            for i, (dx, dy) in enumerate(dirs):
                if (pattern & (1 << i)) > 0:
                    sx, sy = x + dx, y + dy
                    if 0 <= sx < n and 0 <= sy < m and (patterns[grid[sx][sy]] & (1 << ((i + 2) % 4))) > 0:
                        ds.merge(getId(x, y), getId(sx, sy))

        for i in range(n):
            for j in range(m):
                handler(i, j)

        return ds.find(getId(0, 0)) == ds.find(getId(n - 1, m - 1))





