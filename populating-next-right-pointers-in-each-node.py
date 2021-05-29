# """
# Definition for a Node.
# 让每个next指针指向下一个右侧节点
from xlwings import xrange
# 填充每个节点的下一个右侧节点指针

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# """
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
#
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
#

class Solution:
    # def connect(self, root):   #todo 为什么不符合常量的辅助空间的要求？？
    #     """
    #     :type root: Node
    #     :rtype: Node
    #     """
    #     if not root:
    #         return root
    #     queue = [root]
    #     while queue:
    #         size = len(queue)
    #         # 将队列中的元素串联起来
    #         tmp = queue[0]
    #         for i in xrange(1, size):
    #             tmp.next = queue[i]
    #             tmp = queue[i]
    #         # 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
    #         for _ in xrange(size):
    #             tmp = queue.pop(0)
    #             if tmp.left:
    #                 queue.append(tmp.left)
    #             if tmp.right:
    #                 queue.append(tmp.right)
    #     return root
    def connect(self, root):
        if not root:
            return None
        a = [root]
        s = len(a)
        for i in range(s):
            print('>', i, s, a)
            if i < s - 1:
                print('1:', a[i])
                a[i].next = a[i + 1]
            else:
                print('2:', a[i])
                a[i].next = None  # todo next是节点中的next，为什么不行？？
            a.append(a[i].left)
            a.append(a[i].right)
            print(a)
        for j in range(s):
            a.pop(j)
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2 (self, root):  # 递归
        """
        :type root: Node
        :rtype: Node
        """

        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right
            # 配合动画演示理解这段，以root为起点，将整个纵深这段串联起来
            while left:
                left.next = right
                left = left.right
                right = right.left
            # 递归的调用左右节点，完成同样的纵深串联
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root


