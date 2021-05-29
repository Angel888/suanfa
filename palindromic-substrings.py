class Solution:
    def countSubstrings(self, s: str) -> int:
        # todo 哪里有问题，好像计算重复了？
        l = len(s)
        res=0
        for i in range(l):
            sum_1 = self.get_l(s, i, i)
            sum_2 = self.get_l(s, i, i + 1)
            res+=(sum_1+sum_2)
        print(res)
        return res
    def get_l(self, s, a, b):
        l=len(s)
        ret=0
        while a>=0 and b<l and s[a]==s[b]:
            ret+=1
            a-=1
            b+=1
        return ret

    def countSubstrings1(self, s: str) -> int:
        l=len(s)
        dp=[[0]*l for _ in range(l)]
        res=0
        for i in range(l,-1,-1):
            for j in range(i,l):
                if i==j or (i+1==j and s[i]==s[j]) or (i+1<j and dp[i+1][j-1] and s[i]==s[j]):
                    dp[i][j]=True
                    res+=1
        # print(res)
        return res
if __name__ == '__main__':
    s=Solution()
    s.countSubstrings("aaa")
    s.countSubstrings1("aaa")

