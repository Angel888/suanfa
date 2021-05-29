# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
#  方法一：把链表全放到列表里，然后倒着遍历
#  方法二：递归
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):  # todo 错了，是从左往右
        tmp1 = l1
        tmp2 = l2
        tmp4 = ListNode(None)
        tmp3 = tmp4
        a = 0
        tmp_1 = 0
        while tmp1 or tmp2 or tmp_1>0:
            if tmp1 and tmp2:
                a = (tmp1.val + tmp2.val + tmp_1)
            elif tmp1:
                a = (tmp1.val + tmp_1)
            elif tmp2:
                a = (tmp2.val + tmp_1)
            elif tmp_1 > 0 and tmp1 is None and tmp2 is None:
                a = tmp_1
            tmp = a % 10
            tmp_1 = a // 10
            # print("tmp---",tmp)
            tmp3.next = ListNode(tmp)
            tmp3 = tmp3.next
            if tmp1:
                tmp1 = tmp1.next
            else:
                tmp1 = None
            if tmp2:
                tmp2 = tmp2.next
            else:
                tmp2 = None
        # printL(tmp4.next)
        return tmp4.next

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode):
        tmp1 = l1
        tmp2 = l2
        tmp4 = ListNode(None)
        tmp3 = tmp4
        self.addTwoNumbers2(tmp1, tmp2, 0, tmp3)
        printL(tmp4)
        return tmp3

    def get_tmp_next(self, a, b):
        if a is None and b is not None:
            c = ListNode(0)
            d = b.next
        elif b is None and a is not None:
            d = ListNode(0)
            c = a.next
        elif a is not None and b is not None:
            c = a.next
            d = b.next
        else:
            return None, None
        return c, d

    def addTwoNumbers2(self, tmp1, tmp2, val, tmp5):
        tmp3 = tmp5
        c, d = self.get_tmp_next(tmp1, tmp2)
        if c is None and d is None:
            return 0
        tmp_1 = self.addTwoNumbers2(c, d, val, tmp3)  # todo 递归
        tmp_0 = (c.val + d.val) % 10
        tmp_1 = (c.val + d.val) // 10
        tmp3.next = ListNode(tmp_0)

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode):  # todo 除了递归还能用别的办法吗
        tmp1 = l1
        tmp2 = l2
        tmp4 = ListNode(None)
        tmp3 = tmp4
        while tmp1.next:
            tmp1 = tmp1.next
        while tmp2.next:
            tmp2 = tmp2.next
        tmp_0 = (tmp1 + tmp2) % 10
        tmp_1 = (tmp1 + tmp2) // 10
        self.addTwoNumbers3()  # #


def printL(head):
    while head.next and head:
        print(head.val)
        print('->')
        head = head.next
    print(head.val)


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    Solution().addTwoNumbers(l1, l2)
    # Solution().get_tmp_next(l1,l2)
