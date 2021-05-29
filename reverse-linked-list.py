# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if head.next:
            head1 = self.reverseList(head.next)
            head.next = head.next.next
            return head1
        else:
            return head

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while head:
            # 记录当前节点的下一个节点
            tmp = head.next
            # 然后将当前节点指向pre
            head.next = pre
            # pre和head节点都前进一位
            pre = head
            head = tmp
        return pre

    def reverseList2(self, head):
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

    def reverseList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)  # todo 为什么不需要while，加上while因能给过
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

    def reverseList4(self, head):
        if head.next is None or head is None:
            return head
        cur = self.reverseList(head.next)   # 每次都返回前一个节点的办法应该是不可以，只能在每次执行完成后返回最后一个节点
        cur.next = head
        head.next=None

    def reverseList5(self, head: ListNode) -> ListNode:
        def helper(head):
            if head == None or head.next == None:
                return head, head
            pre, last = helper(head.next)   # pre是用来传递头的
            last.next = head
            head.next = None
            return pre, head

        rt, _ = helper(head)
        return rt

if __name__ == '__main__':
    Solution().reverseList()
    """
    ListNode reverse(ListNode head) {
    if (head.next == null) return head;
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return last;
}
"""
