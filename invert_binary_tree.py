# https://leetcode-cn.com/problems/invert-binary-tree/   翻转二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':  #todo 怎样测试？？
    Solution().invertTree()

