# https://leetcode-cn.com/problems/surrounded-regions/

# 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；

# 对于O的要求：不在边界上，或者不跟边界上的O相连
# X X X X
# X O O X
# X X O X
# X O X X

class Solution:
    def solve(self, board: [[]]):
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):  # x是竖着的坐标,y是横着的坐标
            # 标记成A的条件：为O，并且在board范围内
            # todo 为什么需要标记为A？为了筛选出需要变X的点
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            # # A代表的是和边缘相连的O
            board[x][y] = "A"
            # 以该点为中心，上下左右走
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":  
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
