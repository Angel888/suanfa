import re

class Solution:
    def replaceSpace(self, s) -> str:
        re.sub(r" ","20%",s)  # todo 正则怎么做？
        return s

    def replaceSpace1(self, s) -> str:
        return "20%".join(s.split())

    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a=0
            b=1
            for i in range(2,n+1):
                tmp=b
                b=a+b
                a=tmp
            return b
if __name__ == '__main__':
    s=Solution()
    # print(s.replaceSpace("We are happy."))
    print(s.replaceSpace1("We are happy."))
