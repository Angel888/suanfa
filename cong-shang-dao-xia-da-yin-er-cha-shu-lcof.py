# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        s=[root]
        a=[]
        while s:
            s.append(s[0].left) if s[0].left else None
            s.append(s[0].right) if s[0].right else None
            a.append(s.pop(0).val )
        return a



