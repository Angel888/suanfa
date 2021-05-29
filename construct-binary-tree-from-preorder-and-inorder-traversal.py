# Definition for a binary tree node.
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# todo 当只有一个节点或者无节点时返回什么？节点是怎么连起来的？
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def dfs(preorder,inorder):
            if not preorder:
                return
            print(preorder,inorder)
            if len(preorder)==1:
                root=TreeNode(preorder[0])
                return root
            i=inorder.index(preorder[0])
            p=preorder.index(inorder[0])
            root=TreeNode(preorder[0])
            root.left=dfs(preorder[1:p],inorder[:i])
            root.right=dfs(preorder[p+1:],inorder[i+1:])
            return root
        return dfs(preorder,inorder)

    def buildTree1(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)

    def buildTree3(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: idx + 1], inorder[0: idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1: ])
        return root
    def buildTree4(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        inorder_index=inorder.index(preorder[0])   # 前序列表的第一个元素在中序列表的位置
        root.left=self.buildTree4(preorder[1:inorder_index+1],inorder[:inorder_index])
        root.right=self.buildTree4(preorder[inorder_index+1:],inorder[inorder_index+1:])

# 输入：
# [1,2,3]
# [2,3,1]
# 输出：
# [1,2,3]
# 预期结果：
# [1,2,null,null,3]

if __name__ == '__main__':
    s=Solution()
    s.buildTree([3,9,20,15,7],[9,3,15,20,7])
    s.buildTree1([3,9,20,15,7],[9,3,15,20,7])
