# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

# 动态规划经常会有从后往前推的思维模式
#1注意要分不同情况讨论
# 2 直接使用res,减少时间复杂度
# 对于动态规划，找到递归的公式很重要！
#todo 再做一遍
class Solution:
    def maxValue(self, grid):
        h = len(grid)
        l = len(grid[0])
        res = [[0] * (l) for _ in range(h)]
        res[0][0] = grid[0][0]
        res[0][1] = grid[0][1] + grid[0][0]
        res[1][0] = grid[1][0] + grid[0][0]
        for i in range(1, h):
            for j in range(1, l):
                res[i][j] = max(res[i][j - 1], res[j][i - 1]) + grid[i][j]
        print("res---",res)
        return res[-1][-1]

    def maxValue1(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
if __name__ == '__main__':
    s=Solution()
    grid=[[1,3,1],[1,5,1],[4,2,1]]
    print(s.maxValue(grid))
    print(s.maxValue1(grid))