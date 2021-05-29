# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) :
        # self.isValidBST(root.left)
        self.val=-float("inf")
        def dfs(root):
            if not root:
                return True
            self.val=dfs(root.left)
            if self.val>=root.val:
                return False
            self.val=dfs(root.right)
            return True
        dfs(root)

