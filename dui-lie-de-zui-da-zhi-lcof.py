# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
# 输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,null,2]
# 预期结果：[null,null,null,2,1,2]
# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
# todo 为什么栈可以使用最小值变量，队列不可以用最大值变量
# 因为栈是先进后出，最大值先进去，后面的值出的时候最大值不会出；而队列是先进先出
# 关于求最大值：
# 之前的方法是每次push都和当前最大值比较，小于最大值则抛弃，这样会导致当最大值出队列时，找不到次大的值。而栈是先进后出的，在后面小的值出栈后，最大值才会出栈，这样比较完全ok。
# 所以这次应该是每次v进队列时，去掉比较队列中比v小的，因为v一定在这些值之后出队，只要有v，这些值就不会是max
# todo 为sm都从最右开始比？因为append是添加到最右
import collections


class MaxQueue:

    def __init__(self):
        self.A, self.B = collections.deque(), collections.deque()

    def max_value(self) -> int:  #
        return self.B[0] if self.B else -1

    def push_back(self, value: int) -> None:
        self.A.append(value)
        while self.B and self.B[-1]< value:
            self.B.pop()
        # if not self.B or self.B[-1] <= value:
            self.B.append(value)

    # def pop_front(self) -> int:
    #     if not self.B:
    #         return -1
    #     if self.A:
    #         a = self.A.popleft()
    #         if a == self.B[-1]:
    #             return self.B.pop()
    #         return a
    #     return -1
    def pop_front(self) -> int:
        if not self.A: return -1
        ans = self.A.popleft()
        if ans == self.B[0]:  #todo
            self.B.popleft()
        return ans



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

# [null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,null,871,871,871,646,null,null,null,null,229,871,646,285,45,646,null,null,140,null,null,null,null,837,806,null,806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,806,null,674,null,null,770]
# [null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,null,871,871,871,646,null,null,null,null,229,871,"837",285,45,837,null,null,140,null,null,null,null,837,806,null,806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,770,null,674,null,null,770]
