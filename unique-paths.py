class Solution:
    def uniquePaths(self, m: int, n: int):
        dp=[[0 for i in range(n) ] for j in range(m)]
        for a in range(n):
            dp[0][a]=1
        for b in range(m):
            dp[b][0]=1
        dp[1][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n][m]
if __name__ == '__main__':
    s=Solution()
    print(s.uniquePaths(m = 3, n = 7))