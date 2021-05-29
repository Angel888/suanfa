class CQueue:

    def __init__(self):
        self.l_1=[]
        self.l_2=[]

    def appendTail(self, value: int) -> None:
        self.l_1.append(value)
        return

    def deleteHead(self) -> int:
        if self.l_2:
            return self.l_2.pop()
        while self.l_1:
            self.l_2.append(self.l_1.pop())
        if self.l_2:
            return self.l_2.pop()
        return -1

class CQueue1:

    def __init__(self):
        self.l_1=[]
        self.l_2=[]

    def appendTail(self, value: int) -> None:
        self.l_1.append(value)
        self.l_2.append(self.l_1.pop(0))
        return

    def deleteHead(self) -> int:
        if len(self.l_2)>0:
            return self.l_2.pop()
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()