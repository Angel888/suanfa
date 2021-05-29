# Definition for a binary tree node.
# https://leetcode-cn.com/problems/list-of-depth-lcci/
from _ast import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> list:
        if tree is None:
            return []
        res = []  # 结果集
        queue_list=[TreeNode]
        while queue_list!=[]:
            layer=[]
            for i in queue_list:
                queue_list.append(i.left)
                queue_list.append(i.right)
                layer.append(i.val)
            res.append(layer)
















{
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}














    def listOfDepth1(self, tree: TreeNode) -> list:

        if tree is None:
            return []
        res = []  # 结果集
        temp = deque()
        temp.append(tree)
        while len(temp) > 0:  # BFS模板开始
            tmp_dummy_node = ListNode(None)  # 创建dummynode
            cur = tmp_dummy_node
            next_layer = []  # 存储下一层元素
            while len(temp) != 0:  # 将某一层中的全部取出处理
                node = temp.popleft()
                cur.next = ListNode(node.val)  # 将一层中的组合成链表
                cur = cur.next
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            res.append(tmp_dummy_node.next)  # 压入结果集
            temp = deque(next_layer.copy())
        return res


