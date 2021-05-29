# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) :
        if not root:
            return True
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            # if not left:   #todo "not 0"和 "is False"不一样  not 是!=
            if left is False:
                return False
            right=dfs(root.right)
            if not right:
                return False
            if abs(right-left)<=1:
                return max(left,right)+1 # todo
            return False
        return dfs(root)


