# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
