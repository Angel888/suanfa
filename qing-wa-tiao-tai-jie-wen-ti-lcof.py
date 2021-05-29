# https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
#  注意f（n-2）时不要重复计算f(n-1)的情况
#  大数越界！
class Solution:
    def numWays(self, n: int) -> int:
        res=[1,1,2]
        if n<3:
            return res[n]
        for i in range(3,n+1):
            res.append(res[i-2]+res[i-1])
        print("res--",res)
        return res[-1]
if __name__ == '__main__':
    s=Solution()
    print(s.numWays(45))

# 7,21