# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        if not B:
            return False
        return self.frontTraverse(A, B)
    def frontTraverse(self,A,B):
        if not A:
            return False
        if self.compare(A,B) or self.frontTraverse(A.left,B) or self.frontTraverse(A.right,B):
            return True
        return False
    def compare(self,A,B):
        if B and (not A):
            return False
        if (not B) and A:
            return True
        if (not A) and (not B):
            return True
        if A.val==B.val:
            if self.compare(A.left,B.left) and self.compare(A.right,B.right):
                return True
        return False

    # def frontTraverse1(self, A, B):
    #     if not B:
    #         return True
    #     if not A:
    #         return False
    #     if A.val == B.val:
    #         print(A.val,B.val)
    #         if self.frontTraverse(A.left, B.left):
    #             return True
    #         if self.frontTraverse(A.right, B.right):
    #             return True
    #     else:
    #         if self.frontTraverse(A.left, B):
    #             return True
    #         if self.frontTraverse(A.right, B):
    #             return True


if __name__ == '__main__':
    # [3, 5, 0, 3, 4]
    # [1, -4, 2, -1, 3, -3, -4, 0, -3, -1]
    A = TreeNode(1)
    A.left = TreeNode(0)
    A.right = TreeNode(1)
    A.right.left = TreeNode(-4)
    A.right.right = TreeNode(-3)
    B = TreeNode(1)
    B.left = TreeNode(-4)
    s = Solution()
    print(s.isSubStructure(A, B))

# [1,0,1,-4,-3]
# [1,-4]
