class Solution:
    # Definition for a binary tree node.
    #todo  前序遍历根节点到p和到q的两个路径（注意剪枝） 然后两个路径逐个比对
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    class Solution:  #todo 是否会有一个节点存在，另一个节点不存在的情况
        def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            TreeNode(9)
            # root为空时，返回的也是空
            if not root or root.val == q.val or root.val == p.val:
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            if not left:
                return right
            if not right:
                return left
            return root
