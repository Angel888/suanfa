# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# todo python用栈和用队列有啥区别
# todo 如果只有左子树或者只有右子树怎么办？
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stk=[]
        stk.append(root.left)
        stk.append(root.right)
        if not root.left or not root.right or root.left.val!=root.right.val:
            return False
        while stk:
            b=stk.pop(0)
            c=stk.pop(0)
            if b.val!=c.val:
                return False
            stk.append(b.left)
            stk.append(c.right)
            stk.append(b.c.right)
            stk.append(c.left)
        return True



