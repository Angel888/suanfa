# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/ todo

from nltk import collections

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A,self.B=[],[]

    def push(self, x: int) -> None:  #todo 每次push，如果push的值比当前值小，则push
        self.A.append(x)
        if not self.B or self.B[-1]>=x:
            self.B.append(x)


    def pop(self) -> None:
        if self.A.pop()==self.B[-1]:
            self.B.pop()


    def top(self) -> int:
        return self.A[-1]


    def min(self) -> int:
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()