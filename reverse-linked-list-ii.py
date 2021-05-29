# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
class Solution:
    # def reverseBetween(self, head, m: int, n: int):
    #     i=0
    #     while i<=n+1:
    #         i+=1
    #         if i==m-1:
    #             pre1=head
    #             head=head.next
    #         elif i==m:
    #             pre2=head
    #             head = head.next
    #         elif n >i>m:
    #             tmp=head.next
    #             head.next=pre2
    #             pre2=head
    #             head=tmp
    #         elif i==n:
    #             tmp = head.next
    #             pre2.next=tmp
    #             head.next = pre2
    #
    #             pre1.next=head
    #             head.next = pre2
    #             tmp1=head.next
    #             head.next=pre2
    #             pre2.next=head
    #
    #     return head

    def reverseFront(self, head, m):  # todo 反转链表前N个节点中，；临界点的next不知道怎么搞，使用遍历的方法似乎不行，会有两个next？
        if head == None or head.next == None:
            return head
        pre = head
        i = 0
        while i < m - 1:
            tmp = head.next
            head.next.next = head
            head.next = None
            head = tmp
        tmp = head.next
        pre.next = head.next

    # Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # def reverseBetween(self, head:, m: int, n: int):
    #     if head is None or head.next is None:
    #         return head
    #     i=1
    #     pre=head
    #     while i<m:
    #         pre=pre.next
    #         i+=1
    #     after=pre.next
    #     while i <=n:
    # successsor = None

    # def reverseFrontN(self, head, n):
    #     """
    #     使用递归的方式找到下一个head.next
    #     :param head:
    #     :param n:
    #     :return:
    #     """
    #     p = n
    #     if p == 1:
    #         self.successsor = head.next
    #         return head
    #     else:
    #         last = self.reverseFrontN(head.next, p - 1)
    #         head.next.next = head
    #         if p == n:
    #             head.next = self.successsor
    #             print(last.val)
    #         return last

    def reverseTailInsert(self, head, m, n):
        """
         试试尾插法
        :param head:
        :param n:
        :return:
        """
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            tmp = head.next
            head.next = None
            tmp.next = head
            printL(tmp)
            return tmp
        if m == n:
            return head
        i = 0
        gap = n - m
        head0 = ListNode(None)  #todo 为啥有了head0就不需要判断了？？
        head0.next=head
        head1=head0
        while i < m - 1:  # m=3 n=6    1,2,3,4,5,6,7,8,9
            i += 1
            head1 = head1.next
        gap_1 = gap
        while gap_1 > 0:
            tmp1 = head1  # tmp1=2
            b = 0
            while b <= gap_1:
                tmp1 = tmp1.next
                b += 1
            tmp3 = head1.next
            tmp4 = tmp1.next
            head1.next = head1.next.next
            tmp1.next = tmp3
            tmp3.next = tmp4
            gap_1 -= 1
        # printL(head0.next)
        return head0.next

    """
    ListNode reverseBetween(ListNode head, int m, int n) {
    // base case
    if (m == 1) {
        return reverseN(head, n);
    }
    // 前进到反转的起点触发 base case
    head.next = reverseBetween(head.next, m - 1, n - 1);
    return head;
}
    """

    # def reverseBetween(self, head: ListNode, m: int, n: int):



def printL(head):
    while head.next and head:
        print(head.val)
        print('->')
        head = head.next
    print(head.val)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next.next.next = ListNode(8)
    # head.next.next.next.next.next.next.next.next = ListNode(9)
    # printL(head)
    # print(Solution1().reverseFrontN(head, 3))  #反转链表的前n个
    # Solution1().reverseTailInsert(head, 3, 6)  # 反转链表的n~m个
    Solution1().reverseTailInsert(head,2,3)  # 反转链表的n~m个
    # Solution1().reverseTailInsert(head,1,1)  # 反转链表的n~m个
    # Solution1().reverseTailInsert(head, 1, 2)  # 反转链表的n~m个
