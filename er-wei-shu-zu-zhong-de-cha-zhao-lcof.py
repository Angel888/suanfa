# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        h = len(matrix)
        l = len(matrix[0])
        # for i in range(h):
        #     for j in range(l,-1,-1):
        if h==0 or l==0:
            return False
        i = 0
        j = l - 1
        while -1 < i < h and -1 < j < l:
            if matrix[i][j] < target:
                j += 1
            if matrix[i][j] > target:
                i -= 1
            if matrix[i][j] == target:
                return True
        return False
