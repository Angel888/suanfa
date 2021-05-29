# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
"""

"""


# 是否可以先通过前序遍历放到列表里，再遍历列表，添加箭头
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def front_traverse(self, root, a):
        if not root:
            return a
        if root.left:
            self.front_traverse(root.left, a)
        a.append(root)
        if root.right:
            self.front_traverse(root.right, a)
        return a

def printV(self, L):
    v = []
    for i in L:
        v.append(i.val)
    return v

    # def dfs(self, root):
    #     if not root: return
    #     self.dfs(root.left)  # 左
    #     print(root.val)  # 根
    #     self.dfs(root.right)  # 右

    def treeToDoublyList(self, root: 'Node'):
        if not root: return
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def dfs(self, cur):
        if not cur: return
        self.dfs(cur.left)  # 递归左子树
        if self.pre:  # 修改节点引用
            self.pre.right, cur.left = cur, self.pre
        else:  # 记录头节点
            self.head = cur
        self.pre = cur  # 保存 cur
        self.dfs(cur.right)  # 递归右子树

    def treeToDoublyList2(self, root):
        def dfs(root, pre, head):
            print(root.val, head.val)
            if root.left:
                pre, head = dfs(root.left, pre, head)
            if not head:
                head = root  # todo 函数是不是不能传None，为什么总是走不到这个逻辑？？
                print("!!!", head.val)
            else:
                pre.right = root
                root.left = pre
            pre = root
            # print("pre",pre.val)
            if root.right:
                pre, head = dfs(root.right, pre, head)
            # print("pre, head---",pre.val, head.val)
            return pre, head

        a, b = dfs(root, Node(None), Node(None))
        print("b~~", b.val)
        # print("a~~", a.val)
        return b

    def treeToDoublyList3(self, root):
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            if not self.head:
                self.head = root
            else:
                self.pre.right = root
                root.left = self.pre
            self.pre = root
            if root.right:
                dfs(root.right)

        self.pre = None
        self.head = None
        dfs(root)
        # print("self.pre.val---",self.pre.val)
        # print("self.head.val---",self.head.val)
        if root:
            self.head.left = self.pre
            self.pre.right = self.head
        # print("self.head.val~~", self.head.val)
        return self.head


class Solution1:
    a = []

    def front_traverse(self, head, a):  # todo 按照这个程序遍历一遍二叉树
        def treeToDoublyList(self, root):
            """"
            中序遍历，每个节点的左指针指向上一个节点；上一个节点的右指针指向该节点
            """

            def dfs(root):
                if not root:
                    return
                if root.left:
                    dfs(root.left)
                if not self.head:
                    self.head = root
                else:
                    self.pre.right = root
                    root.left = self.pre
                self.pre = root
                if root.right:
                    dfs(root.right)

            self.pre = None
            self.head = None
            # print("self.pre.val---",self.pre.val)
            # print("self.head.val---",self.head.val)
            if not root:
                return
            dfs(root)
            self.head.left = self.pre
            self.pre.right = self.head
            # print("self.head.val~~", self.head.val)
            return self.head

    def treeToDoublyList1(self, root):
        self.pre = None
        self.head = None
        self.dfs(root)
        if self.pre and self.head :
            self.pre.right = self.head
            self.head.left = self.pre
        return self.head

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if not root.left and not self.head:
            self.head = root
        else:
            self.pre.right = root
            root.left = self.pre
        self.pre = root
        self.dfs(root.right)
def printV1(head):
    a=[head.val]
    b=head.right
    print(a)
    while b:
        a.append(b.val)
        b=b.right
    print(a)

if __name__ == '__main__':
    s = Solution()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    # print(s.printV(s.front_traverse(root,[])))
    # print(s.treeToDoublyList2(root))
    # b = s.treeToDoublyList3(root)
    # while b:
    #     if root and root.left and root.right:
    #         print("~~~~~",root.val, root.left.val, root.right.val)
    #     b = b.right
    Solution1().treeToDoublyList1(root)
    print(root.left.left.left.val)
    printV1(root.left.left.left)
    printV1(root.left.left)

