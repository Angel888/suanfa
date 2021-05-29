# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
class Solution:
    def buildTree(self, preorder, inorder) :
        i=0
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            # print("preorder[0]--",preorder[0])
            return TreeNode(preorder[0])
        while inorder[i] !=preorder[0] :
            # print("i",i)
            i+=1
        # print("i-----",i)
        a=self.buildTree(preorder[1:i+1],inorder[:i])
        # print("a",a.val)
        b=self.buildTree(preorder[i+1:],inorder[i+1:])
        # print("b", b.val)
        c=TreeNode(preorder[0])
        c.left=a
        c.right=b
        return c

if __name__ == '__main__':
    a=TreeNode(3)
    a.left=TreeNode(9)
    b=TreeNode(20)
    a.right=b
    b.left=TreeNode(15)
    b.right=TreeNode(7)
    s=Solution()
    print(s.buildTree(preorder = [3,9,20,15,7],inorder = [9,3,15,20,7]))