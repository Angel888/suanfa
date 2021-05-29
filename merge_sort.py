def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# a=[6，202，100，301，38，8，1]
def mergeSort1(arr):
    """
    :param arr: list
    :return: 排序后的list
    """
    left=0
    right=len(arr)
    if right-left>1:
        middle=(left+right)//2
        com_arr(mergeSort1(arr[left:middle]),mergeSort1(arr[middle:right]))
def com_arr(left,right):
    """
    :param left: list_1
    :param right: list_2
    :return: 一个list
    """
    res=[]
    while left and right:
        if left[0]<=right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res+=left
    elif right:
        res+=right
    return res
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList3(self, head):
        """
        对于每一个段链表的处理，都是先分成拆分最小的两部分，然后再排序，返回排序后的结果；
        排序后的链表又组成一个left或rght
        :param head:
        :return:
        """
        if not head or not head.next: return head # termination.
        slow, fast = head, head.next
        # 将链表分成两部分
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # 两部分循环切割
        left, right = self.sortList3(head), self.sortList3(mid)
        h = res = ListNode(0)  #h是一个运动的节点
        # 比较切割后的两个链表
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
    def sortList2(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1  # h指向最后一个链表节点，length为链表长度
        res = ListNode(0)   # 初始化的链表节点指向head
        res.next = head
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

    def sortList4(self, head):  # todo 再做一遍
        if not head or not head.next: return head
        fast=head.next
        slow=head
        while fast and fast.next :
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        slow.next=None
        left,right=self.sortList4(head),self.sortList4(mid)   #left,fight 是已经排序好了的链表
        res=tmp=ListNode(0)
        while left and right:
            if left.val<right.val:
                tmp.next = left
                left=left.next
            else:
                tmp.next=right
                right=right.next
            tmp = tmp.next
        if left:
            tmp.next=left
        if right:
            tmp.next = right
        return res.next

if __name__ == '__main__':
    s=Solution()
    p1=ListNode(-1)
    p1.next=ListNode(5)
    p1.next.next=ListNode(3)
    p1.next.next.next=ListNode(4)
    p1.next.next.next.next=ListNode(0)
    s.sortList4(p1)








