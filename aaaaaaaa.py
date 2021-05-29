"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not node.left and not self.head:
                self.head = node
            else:
                self.pre.right = node
                node.left = self.pre
            self.pre = node
            dfs(node.right)

        self.pre = None
        self.head = None
        dfs(root)
        # print(self.head)
        # return 
        if self.pre and self.head:
            self.pre.left = self.head
            self.head.right = self.pre
        return self.head




"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        self.pre = None
        self.head = None
        self.dfs(root)
        # print(self.head)
        # return
        # if self.pre and self.head:
        #     self.pre.left = self.head
        #     self.head.right = self.pre
        return self.head

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if not node.left and not self.head:
            self.head = node
        else:
            print(node.val, self.pre.val)
            self.pre.right = node
            node.left = self.pre
        self.pre = node
        print(self.pre.val, node.right)
        self.dfs(node.right)
