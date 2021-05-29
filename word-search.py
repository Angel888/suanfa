# https://leetcode-cn.com/problems/word-search/
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
# 思路：每个点

class Solution:
    def exist(self, board, word) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:  # 以a点为例，如果这个点的上下左右都没有匹配到下一个，那么a点是FALSE
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:  # 遍历四个方向
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):  # 要在board内
                    if (newi, newj) not in visited:  # 前面没有使用过这个值
                        if check(newi, newj, k + 1):
                            print("visited!!", visited)
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])  # 竖着，横着
        visited = set()
        for i in range(h):
            for j in range(w):  # 从左到右，从上到下遍历
                if check(i, j, 0):
                    print("a")
                    return True
        print("b")
        return False

    def exist1(self, board, word):
        def check(i, j, location, used_word):
            if board[i][j] == word[location] and location == w - 1:
                return True
            elif board[i][j] == word[location] and location < w - 1:
                location+=1
                used_word.append((i, j))
                for c, d in directions:
                    new_i = i + c  # 竖
                    new_j = j + d
                    # print("new_i,new_j~~~~~~", i, j, new_i, new_j, location)
                    if 0 <= new_i < a and 0 <= new_j < b and (new_i, new_j) not in used_word:
                        if check(new_i, new_j, location, used_word):
                            return True  # todo  如果缺了break会是神马 结果？
                    # print("new_i,new_j~~~~~~",i,j,new_i,new_j,location)
                # print("remove~~",i,j )
                used_word.remove((i, j))
                return False
            else:
                return False

        w = len(word)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        used_word = []
        a = len(board)  # 竖
        b = len(board[0])
        for i in range(a):
            for j in range(b):
                if check(i, j, 0, used_word):
                    # print("a")
                    return True
        # print("b")
        return False


if __name__ == '__main__':
    Solution().exist(board=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word="ABCCED")
    Solution().exist1(board=[['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word="ABCCED")
