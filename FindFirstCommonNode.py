class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            print(str(p1), str(p2))
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1


if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    print(Solution().FindFirstCommonNode(a1, a3).val)
