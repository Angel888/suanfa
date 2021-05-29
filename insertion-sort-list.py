# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#todo 自己再做一遍
# 输入: 4->2->1->3
# 输出: 1->2->3->4
class Solution:
    def insertionSortList(self, head):
        dummyHead = ListNode(0)
        dummyHead.next = head
        p1 = head  # 用p1不断地遍历头结点
        while p1 and p1.next:
            if p1.val <= p1.next.val:
                p1 = p1.next
            else:  # 当有前节点<后节点的情况时，从头结点开始遍历，如果有前节点<p1,后节点>p1，则插入到这个位置
                pre = dummyHead
                q = p1.next
                while pre.next.val < q.val:
                    pre = pre.next
                p1.next=q.next
                q.next=pre.next

