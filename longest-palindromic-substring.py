class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_e = len(s)
        ans = ""
        dp = [[False] * l_e for _ in range(l_e)]
        for l in range(l_e):
            for i in range(l_e):
                j = i + l
                if j >= l_e:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] =(dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def longestPalindrome1(self, s: str) -> str:
        """
        使用中心扩散的方法解决
        :param s:
        :return:
        """
        res=""
        a_0,b_0=0,0
        l=len(s)
        for i in range(l):
            a_1,b_1=self.get_l(s,i,i)
            a_2,b_2=self.get_l(s,i,i+1)
            a,b=(a_2,b_2) if b_2-a_2>b_1-a_1 else (a_1,b_1)
            if b_0-a_0<b-a:
                a_0,b_0=a,b
            print(a_0,b_0)
            print(s[a_0:b_0+1])
        return s[a_0:b_0+1]

    def get_l(self,s,a,b):
        l=len(s)
        while a>=0 and b<l:
            if s[a]==s[b]:
                a-=1
                b+=1
            else:
                return a+1,b-1
        return a+1,b-1
    def get_l1(self,s,a,b):
        l=len(s)
        while a>=0 and b<l and s[a]==s[b]:
            a-=1
            b+=1
        return a+1,b-1

if __name__ == '__main__':
    s=Solution()
    s.longestPalindrome1("babad")
