# https://leetcode-cn.com/problems/word-search/
#  偏移量 回溯法
from typing import List

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
from typing import List


# todo 用"SEE"试试，然后自己写一个
class Solution:
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 这里没有变化，用tuple就好

    def exist1(self, board: List[List[str]], word: str):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        marked = [[False for _ in range(n)] for _ in range(m)]  # todo 使用了一个marked来记录，为什么要用marked？？为什么不是一个有一串点的列表？
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index,  
                      start_x, start_y, marked, m, n):
        # 先写递归终止条件
        if index == len(word) - 1:  # 当找到最后一个字母时，判断是否相等
            return board[start_x][start_y] == word[index]

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and \
                        not marked[new_x][new_y] and \
                        self.__search_word(board, word,
                                           index + 1,
                                           new_x, new_y,
                                           marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False

    def exist(self, board: List[List[str]], word: str):
        n = len(board)
        m = len(board[0])
        if m == 0:
            return False
        word = list(word)
        w = len(word)
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 这里没有变化，用tuple就好

        def search_word(a, b, w_0): #todo 这个递归哪里有问题
            print(a,b)
            i = 0
            if 0 <= a < n - 1 and 0 <= b < m - 1 and i < w - 1 and board[a][b] == word[i]:
                for d in directions:
                    a = a + d[0]
                    b = b + d[1]
                    i += 1
                    search_word(a, b, word[i])
            elif a == n - 1 and b == m - 1 and i == w - 1:
                return True
            else:
                return False

        for i in range(n):
            for j in range(m):
                if search_word(i, j, word[0]):
                    return True
        return False


if __name__ == '__main__':
    Solution().exist(board=
    [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], word="ABCCED")
