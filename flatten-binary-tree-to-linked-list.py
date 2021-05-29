# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten(self, root: TreeNode):
        if not root:
            return None
        if root.left:
            root1 = root.left
            while root1.right:
                root1 = root1.right  # root1是左子树最右边的节点
            root2 = root.right  # root2是右子树第一个节点
            root.right = root.left  # 将左子树放在右子树
            root.left = None  # 将根节点的左子树置为空
            root1.right = root2  #将右子树拼接在左子树下面
            self.flatten(root.right)
        else:
            self.flatten(root.right)
        return
"""
public void flatten(TreeNode root) {
    while (root != null) { 
        //左子树为 null，直接考虑下一个节点
        if (root.left == null) {
            root = root.right;
        } else {
            // 找左子树最右边的节点
            TreeNode pre = root.left;
            while (pre.right != null) {
                pre = pre.right;
            } 
            //将原来的右子树接到左子树的最右边节点
            pre.right = root.right;  #todo
            // 将左子树插入到右子树的地方
            root.right = root.left;
            root.left = null;
            // 考虑下一个节点
            root = root.right;
        }
    }
}
"""