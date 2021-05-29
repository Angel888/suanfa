# https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/  todo
# Definition for a binary tree node.  浅拷贝和深拷贝
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))  # todo 是否写list有什么区别？也可以用path[:]
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()  #todo  为什么这里要pop

        recur(root, sum)
        return res

    def pathSum1(self, root, sum):
        res = []
        l = []
        if not root:
            return res

        def recurr(root, sum):  # todo 这种方式的l是怎样append的？
            if not root:  return  # todo 为什么这里直接return?
            sum = sum - root.val
            l.append(root.val)
            if not root.left and not root.right and sum == 0:
                res.append(l)
            if root.left:
                recurr(root.left, sum)
            if root.right:
                recurr(root.right, sum)

        recurr(root, sum)
        return res


class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        l = []
        if not root:
            return self.res
        self.recurr(root, sum - root.val, l)
        return self.res

    def recurr(self, root, sum, l):  # todo 这种传递l的方式为什么不行？
        if root:
            l.append(root.val)
            print("l--", l)
        if not root.left and root.right and sum == 0:
            self.res.append(list(l))
        if root.left:
            self.recurr(root.left, sum - root.left.val, l)
        if root.right:
            self.recurr(root.right, sum - root.right.val, l)
