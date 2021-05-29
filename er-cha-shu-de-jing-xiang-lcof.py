# Definition for a binary tree node.
# todo  https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/ 在做一遍遍
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        root.left,root.right=root.right,root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root

    def mirrorTree1(self, root: TreeNode) -> TreeNode:  # todo 为什么要直接用栈，将两层作为一个单元直接替换可以吗？
        if not root:
            return root
        root.left, root.right = root.right, root.left
        root.left.right.val, root.right.left.val = root.right.left.val, root.left.right.val
        root.right.right.val, root.left.left.val = root.left.left.val, root.right.right.val
        self.mirrorTree(root.left.left)
        self.mirrorTree(root.left.right)
        self.mirrorTree(root.right.left)
        self.mirrorTree(root.right.right)
        return root

    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        stk=[]
        if

