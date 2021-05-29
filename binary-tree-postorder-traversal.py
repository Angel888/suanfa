# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:  # todo
    def postorderTraversal(self, root):
        a = []
        self.post_order(root, a)
        return a

    def post_order(self, root, a):
        if not root:
            return a
        self.post_order(root.left, a)
        self.post_order(root.right, a)
        a.append(root.val)
        return a

    def postorderTraversal1(self, root):
        """
        如果有左节点和根节点就先加到栈里面，没有时再找右节点，输出
        :param root:
        :return:
        """

        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left  # 左节点全都进栈
            root = stack.pop()  # 左节点都进栈之后，再一个一个检查是否需要出栈
            if not root.right or root.right == prev:
                res.append(root.val)  # 当没有右节点/或右节点已经添加？时，根节点添加到res
                prev = root
                root = None
            else:
                stack.append(root)  #
                root = root.right

        return res

    def postorderTraversal2(self, root):
        """
        有左节点就放到栈里面，有右节点就输出到结果
        :param root:
        :return:
        """
        res = []
        stk = []
        prev = None
        if not root:
            return res
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if not root.right or root.right == prev:  # 如果root不被置为None，那么会陷入死循环
                res.append(root)
                prev=root
                root=None
            else:
                stk.append(root)
                root=root.right
        return res
