# https://leetcode-cn.com/problems/search-a-2d-matrix/
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# 输出：true

# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# 输出：false
# 搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)  # 4
        col = len(matrix[0])  # 3
        lenth = row * col  # 12
        left = 0
        right = lenth - 1
        while left <= right:
            mid = left + (right - left) // 2  # todo 单数时mid怎么算？？
            a =(mid+1) // col
            b = mid % col
            if matrix[a][b] < target:
                left = mid + 1
            elif matrix[a][b] > target:
                right = mid - 1
            elif matrix[a][b] == target:
                return True
        return False

    def searchMatrix1(self, matrix, target) :
        if not matrix or not matrix[0]:
            return False
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        array = [column for row in matrix for column in row]
        print(array)
        while left <= right:
            mid = ((right - left) >> 1) + left
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1  # ascending
            else:
                right = mid - 1
        return False



if __name__ == '__main__':
    print(Solution().searchMatrix1(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13))
    # print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=3))
