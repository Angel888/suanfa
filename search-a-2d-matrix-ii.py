class Solution:
    def searchMatrix(self, matrix, target: int):
        high = len(matrix)
        leng = len(matrix[0])
        # if leng<=1:
        #     if target in
        i = high - 1
        j = 0
        while i > -1 and j < leng:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    s.searchMatrix([[1, 1]], 0)
