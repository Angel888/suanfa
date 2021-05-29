# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:   #todo 这样写为什么不对？
        def dfs_depth(root,a,d):
            a+=1
            if root.left:
                b=a
                dfs_depth(root.left,b,d)
            if root.right:
                c=a
                dfs_depth(root.right,c,d)
            else:
                d=max(a,d)
            return d
        if not root:
            return 0
        d=1
        return dfs_depth(root,0,d)

    def maxDepth1(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    def maxDepth2(self, root: TreeNode):
        """
        层序遍历找到最大深度
        :param root:
        :return:
        """
        a=0
        if not root:
            return a
        layer=[root]
        while layer:
            a+=1
            tmp=[]
            for i in layer:
                tmp.append(i.left)
                tmp.append(i.right)
            layer=tmp
        return a


