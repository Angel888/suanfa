# https://leetcode-cn.com/problems/add-two-numbers-ii/
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        tmp1 = l1
        tmp2 = l2
        tmp4 = ListNode(None)
        tmp3 = tmp4
        self.addTwoNumbers2(tmp1, tmp2, 0, tmp3)
        printL(tmp4.next)
        return tmp4.next

    def get_tmp_next(self, a, b):
        if b.next and not a.next:
            c = ListNode(0)
            d = b.next
        elif a.next and not b.next:
            c = a.next
            d = ListNode(0)
        elif a.next and b.next:
            c = a.next
            d = b.next
        else:
            return None, None
        return c, d

    def addTwoNumbers2(self, tmp1, tmp2, val, tmp3):  # todo 完了链表还得反转
        # print("tmp1.val, tmp2.val~~~~~",tmp1.val, tmp2.val)
        c, d = self.get_tmp_next(tmp1, tmp2)
        if c is None and d is None:
            return 0
        tmp_1 = self.addTwoNumbers2(c, d, val, tmp3)  # todo 递归的话，怎样使个位和个位对齐
        # print("c.val,d.val----",c.val,d.val)
        tmp_0 = (c.val + d.val + tmp_1) % 10
        print("tmp_0***", tmp_0)
        tmp_1 = (c.val + d.val + tmp_1) // 10
        tmp3.next = ListNode(tmp_0)
        return tmp_1

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode):
        """
        先分别放到列表里，
        :param l1:
        :param l2:
        :return:
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        var=0
        l3=ListNode(None)
        l4=l3
        ll=[]
        while len(s1)>0 or len(s2)>0 or var>0:
            a=s1.pop() if len(s1)>0 else 0
            b=s2.pop() if len(s2)>0 else 0
            print()
            tmp=a+b+var
            ll.append(tmp%10)
            var=tmp//10
        while len(ll)>0:
            l4.next=ListNode(ll.pop())
            l4=l4.next
        printL(l3.next)
        return l3.next
# ans=None
#     curnode = ListNode(cur)
#     curnode.next = ans
#     ans = curnode   倒着吧链表连起来，很妙！！
#




def printL(head):
    while head.next and head:
        print(head.val)
        print('->')
        head = head.next
    print(head.val)


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    Solution().addTwoNumbers1(l1, l2)
    # Solution().get_tmp_next(l1, l2)
