# https://leetcode-cn.com/problems/matrix-block-sum/
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]

# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
# 给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 
#
# i - K <= r <= i + K, j - K <= c <= j + K 
# K=1,
# r=0,c=0时，i<=1,i>=-1;
# r=0,c=1时，i<1,;  c>=0,j>=0
# (r, c) 在矩阵内。
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100

class Solution:
    def matrixBlockSum(self, mat: [[]], K: int):
        row = len(mat)
        col = len(mat[0])
        res = [[0] * col  for _ in range(row)]
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        dp[0][0] = mat[0][0]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + mat[i-1][j-1]
        for i in range(row):
            for j in range(col):
                k_i0 = max(0,i-K)
                k_j0 = max(0,j-K)
                k_i1 = min(row,i+K+1)
                k_j1 = min(col,j+K+1)
                res[i][j]=dp[k_i1][k_j1]+dp[k_i0][k_j0]-dp[k_i1][k_j0]-dp[k_i0][k_j1]
        return res
if __name__ == '__main__':
    # Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1)
    Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2)
