class Solution:
    def sumNums(self, n):
        return sum(range(n+1))
        # return n and (n + self.sumNums(n - 1))


    # def __init__(self):
    #     self.res = 0
    # def sumNums1(self, n: int) -> int:
    #     n > 1 and self.sumNums(n - 1)
    #     self.res += n
    #     return self.res

if __name__ == '__main__':
    s=Solution()
    print(s.sumNums(3))