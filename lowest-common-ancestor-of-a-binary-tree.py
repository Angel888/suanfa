# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/  todo 二叉树最近的公共祖先
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身

class Solution:
    # def lowestCommonAncestor(self, root, p, q):
    #     if not root or root == p or root == q: return root
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
    #     if not left and not right: return  # 1.
    #     if not left:
    #         # print(right)
    #         return right  # 3.
    #     if not right:
    #         # print(left)
    #         return left  # 4.
    #     return root  # 2. if left and right:

    def lowestCommonAncestor(self, root, p, q):
        if not root :
            return
        if  root == p or root == q:
            return root
        root1=self.lowestCommonAncestor(root.left, p, q)
        root2=self.lowestCommonAncestor(root.right, p, q)
        if not root2 and not root1:
            return
        if root2 and root1:
            return root
        return root2 if root2 else root1





if __name__ == '__main__':
    print(Solution().lowestCommonAncestor([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=5, q=1))
