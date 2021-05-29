# https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/
# 注意终止条件！
# 注意range逆序和边界值
class Solution:
    # def spiralOrder(self, matrix: [[int]]) -> [int]:
    #     if not matrix: return []
    #     l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
    #     while True:
    #         for i in range(l, r + 1): res.append(matrix[t][i])  # left to right
    #         t += 1
    #         if t > b: break
    #         for i in range(t, b + 1): res.append(matrix[i][r])  # top to bottom
    #         r -= 1
    #         if l > r: break
    #         for i in range(r, l - 1, -1): res.append(matrix[b][i])  # right to left
    #         b -= 1
    #         if t > b: break
    #         for i in range(b, t - 1, -1): res.append(matrix[i][l])  # bottom to top
    #         l += 1
    #         if l > r: break
    #     return res
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        l = 0
        r = len(matrix[0])
        u = 0
        d = len(matrix)
        res = []
        while r >l and d >u:
            for j in range(l, r):
                res.append(matrix[u][j])
            u += 1
            if u==d: break
            for i in range(u, d):
                res.append(matrix[i][r - 1])
            r -= 1
            if l==r: break
            for j in range(r - 1, l - 1, -1):
                res.append(matrix[d - 1][j])
            d -= 1
            if u == d: break
            for i in range(d - 1, u - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l == r: break
        return res

# todo 是否可以遍历某一行（列）之后，则删掉
if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))
    # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6]
