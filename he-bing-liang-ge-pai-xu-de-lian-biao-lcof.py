# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:  # todo 为什么这样会超出时间限制？
        a = ListNode(0)
        l = a
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            elif l1.val > l2.val:
                l.next = l2
                l2 = l2.next
                l = l.next
            else:
                l.next = l1

                l = l.next
                l.next = l2
                l = l.next
                print(l1.next)
                print(l.next)
                l1 = l1.next
                l2 = l2.next
        if l2:
            l.next = l2
        else:
            l.next = l1
        return a.next
