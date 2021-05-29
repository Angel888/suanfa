# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = headA
        n2 = headB
        while n1 != n2:
            n1 = n1.next if n1.next else headB   #todo  n1 = n1.next if n1.next else headB 为什么会超出时间限制？
            n2 = n2.next if n2.next else headA
        return n1
    # def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     n1 = headA
    #     n2 = headB
    #     while n1 != n2:
    #         if n1.next:
    #             n1=n1.next
    #         else:
    #             n1=headB
    #         if n2.next:
    #             n2 = n2.next
    #         else:
    #             n2 = headB
    #     return n1