# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head, k: int) :
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        return head[-k]

