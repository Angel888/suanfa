# class Solution:
#     def Find(self, target, array):
#         m=len(array)-1
#         n=len(array[0])-1
#         t=n
#         q=0
#         while t>=0 and q<=m:
#             if array[q][t]<target:
#                 q+=1
#             elif array[q][t]>target:
#                 t-=1
#             else:
#                 return True
#         return False

# 构建乘积数组  #todo
# class Solution:
#     def multiply(self, A):
#         # write code here
#         if not A:
#             return []
#         # 计算前面一部分
#         num = len(A)
#         B = [None] * num
#         B[0] = 1  # todo 为啥？
#         for i in range(1, num):
#             B[i] = B[i-1] * A[i-1]
#         # 计算后面一部分
#         # 自下而上
#         # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
#         tmp = 1
#         for i in range(num-2, -1, -1):
#             tmp *= A[i+1]
#             B[i] *= tmp
#         return B
# 调整数组顺序使奇数位于偶数前面
# class Solution:
#     def reOrderArray(self, array):
#         m=[]
#         n=[]
#         for i in range(len(array)):
#             if array[i]%2==0:
#                 n.append(array[i])
#             else:
#                 m.append(array[i])
#         m.extend(n)
#         return m
# # if __name__ == '__main__':
#     array=[1,2,3,4]
#     p=Solution().reOrderArray(array)
#     print(p)


# 反转链表

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         l = pHead
#         m = pHead.next
#         r = pHead.next.next
#         while r.next:
#             if l==pHead:
#                 l.next=None
#             m.next=l
#             l=m
#             m=r
#             r=r.next
#         r.next=m
#         return r
# if __name__ == '__main__':
#     p=ListNode(1)
#     p.next.val=2
#     p.next.next.val=3
#     p.next.next.val=4
#     n=Solution().ReverseList(p)
#     print(n.val)
# 二叉树的镜像
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 顺时针打印矩阵
# -*- coding:utf-8 -*-
from pip._vendor.msgpack.fallback import xrange

# class Solution:
#
#     # -*- coding:utf-8 -*-
#     # class RandomListNode:
#     #     def __init__(self, x):
#     #         self.label = x
#     #         self.next = None
#     #         self.random = None
#     # class Solution:
#     #     # 返回 RandomListNode
#     #     def Clone(self, pHead):
#     #         head = pHead
#     #         p_head = None
#     #         new_head = None
#     #
#     #         random_dic = {}
#     #         old_new_dic = {}
#     #
#     #         while head:
#     #             # 这些是存
#     #             node = RandomListNode(head.label)
#     #             node.random = head.random
#     #             old_new_dic[id(head)] = id(node)
#     #             random_dic[id(node)] = node
#     #             head = head.next
#     #
#     #             if new_head:
#     #                 new_head.next = node
#     #                 new_head = new_head.next
#     #             else:
#     #                 new_head = node
#     #                 p_head = node  # P_head是一个根节点
#     #
#     #         new_head = p_head
#     #         while new_head:
#     #             if new_head.random != None:
#     #                 new_head.random = r
#     #             new_head = new_head.next
#     #         return p_head
#     # 二叉搜索树与双向链表
#     # class TreeNode:
#     #     def __init__(self, x):
#     #         self.val = x
#     #         self.left = None
#     #         self.right = None
#     # class Solution:
#     #     # 返回 RandomListNode
#     #     def Clone(self, pHead):
#     #         if not pHead:
#     #             return pHead
#     #         if not pHead.left and not pHead.right:
#     #             return pHead
#     #         p=pHead.left
#     #         while p.right:
#     #             p=p.right
#     #         pHead.left=p
#     #         q=pHead.right
#     #         while q.left:
#     #             q=q.left
#     #         pHead.right=q
#     #         while pHead.left:
#     #             pHead=pHead.left
#     #         return pHead
#
#     # -*- coding:utf-8 -*-
#     # class TreeNode:
#     #     def __init__(self, x):
#     #         self.val = x
#     #         self.left = None
#     #         self.right = None
#     # class Solution:
#     #     def Convert(self, pRootOfTree):
#     #         if not pRootOfTree:
#     #             return pRootOfTree
#     #         if not pRootOfTree.left and not pRootOfTree.right:
#     #             return pRootOfTree
#     #         # 处理左子树
#     #         self.Convert(pRootOfTree.left)
#     #         left = pRootOfTree.left
#     #
#     #         # 连接根与左子树最大结点
#     #         if left:      # todo  这一句是干啥的？？
#     #             while (left.right):   #不断寻找左子树最右边的子树
#     #                 left = left.right
#     #             pRootOfTree.left, left.right = left, pRootOfTree #把根节点的左子针指向左子树最右边的子树；todo 但是left.right不需要再指向根节点了把？？？更何况哪有这么多left.right???
#     #
#     #         # 处理右子树
#     #         self.Convert(pRootOfTree.right)
#     #         right = pRootOfTree.right
#     #
#     #         # 连接根与右子树最小结点
#     #         if right:
#     #             while (right.left):
#     #                 right = right.left
#     #             pRootOfTree.right, right.left = right, pRootOfTree
#     #
#     #         while (pRootOfTree.left):
#     #             pRootOfTree = pRootOfTree.left
#     #         return pRootOfTree
#
#     # 快速排序
#
#     # def quickSort(ll):
#     #     mid=ll[0]
#     #     i=0
#     #     j=len(ll)-1
#     #     while i+1!=j:
#     #         while i<mid:
#     #             i+=1
#     #         while j>mid:
#     #             j-=1
#     #         tmp=ll[i]
#     #         ll[i]=ll[j]
#     #         ll[j]=tmp
#     #     ll.insert(i+1,ll[0])
#     #     ll.pop(0)
#     #     left=quickSort(ll[:i])
#     #     right=quickSort(ll[j+1:])
#     #     return ll
#     # if __name__ == '__main__':
#     #     ll=[5,3,4,7,1,9,2]
#     #     print(quickSort(ll))
#
#     #  连续子数组的最大和
#     # class Solution:
#     #     def FindGreatestSumOfSubArray(self, array):
#     #         max_num=-0x_ffffff
#     #         sum_num=0
#     #         for i in array:
#     #             if sum_num<=0:
#     #                 sum_num=i
#     #             else:
#     #                 sum_num+=i
#     #                 if max_num<sum_num:
#     #                     max_num=sum_num
#     #         return max_num
#     # if __name__ == '__main__':
#     #     aa=[1,-2,3,10,-4,7,2,-5]
#     #     print(Solution().FindGreatestSumOfSubArray(aa))
#
#     # -*- coding:utf-8 -*-
#     # class Solution:
#     #     def PrintMinNumber(self, numbers):
#     #         # write code here
#     #         if not numbers:
#     #             return ""
#     #         lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
#     #         array = sorted(numbers, cmp=lmb)
#     #         return ''.join([str(i) for i in array])
#
#     # 丑数
#     # -*- coding:utf-8 -*-
#
#     # 数组中的逆序对
#     # class Solution:
#     #     def InversePairs(self, data):
#     #         right=len(data)
#     #         left=0
#     #         mid = (left + right) / 2
#     #         i=0
#     #         ll=self.InversePairs(data[left:mid])
#     #         lr=self.InversePairs(data[mid:right])
#     #         res=[]
#     #         while ll and lr:
#     #             if ll[0]<lr[0]:
#     #                 res.append(ll.pop(0))
#     #             else:
#     #                 res.append(lr.pop[0])
#     #                 i+=1
#     #         res+=ll
#     #         res+=lr
#
#     # 数组中的逆序对  todo  没通过
#     def InversePairs(self, data):
#         sortDate = sorted(data)
#         res = 0
#         # for i in sortDate:
#         #     p = data.index(i)
#         #     for j in data[:p]:
#         #         if j > i:
#         #             res += 1
#         #     data.pop(p)
#         # return res
#         for i in sortDate:
#             p = data.index(i)
#             res += p
#             data.pop(p)
#         return res

# if __name__ == '__main__':
#     data = [1,2,3,4,5,6,7,0]
#     ss = Solution()
#     print(ss.InversePairs(data))

# def quick_sort(self, data):
#     if len(data) < 2:
#         return data
#     left = self.quick_sort([i for i in data[1:] if i <= data[0]])
#     right = self.quick_sort([j for j in data[1:] if j > data[0]])
#     return left + [data[0]] + right
# if __name__ == '__main__':
#     data=[3,8,6,5,2,7,4,1]
#     print(quick_sort(data))

# 和为S的连续正数序列
#
# class Solution:
#     #     # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     #     # 函数返回True/False
#     def duplicate(self, numbers, duplication):
#         # 计数排序思想
#         d = {}
#         for i in numbers:
#             if i in d:
#                 d[i] += 1
#                 if d[i] > 1:
#                     duplication.insert(0, i)
#                     return True
#             else:
#                 d[i] = 1
#         return False
#
#         # 无脑算法
#         for i in numbers:
#             if numbers.count(i) > 1:
#                 duplication.insert(0, i)
#                 return True
#         return False
#         # n=len(numbers)
#         # for i in range(n):
#         #     for j in range(i+1:n):
#         #         if numbers[i]==numbers[j] :
#         #             duplication.insert(0,numbers[i])
#         #             return True
#         # return False


# if __name__ == '__main__':
#     duplication = []
#     print(Solution().duplicate([2, 3, 1, 0, 2, 5, 3], duplication))
#     print(duplication)

#  归并排序   todo 列表哪里写错了？
# def cmm(arr1, arr2):
#     i=0
#     j=0
#     arr=[]
#     while arr2 and arr1:
#         # print(arr1, i, arr2, j)
#         if arr1[i]<arr2[j]:
#             arr.append(arr1.pop(0))
#         else:
#             arr.append(arr2.pop(0))
#     if arr1:
#         return arr+arr1
#     elif arr2:
#         return arr+arr2
#
# def s(arr1, arr2):
#     # 跳出条件
#     if not arr1:
#         return arr2
#     if not arr2:
#         return arr1
#     if len(arr1)==1 and len(arr2)==1:
#         return arr1+arr2 if arr1[0] < arr2[0] else arr2+arr1
#     # 分割
#     # 左边的
#     right = len(arr1)
#     left = 0
#     mid = (left + right) // 2
#     a1 = s(arr1[left:mid], arr1[mid:right])
#     # 右边
#     right = len(arr2)
#     left = 0
#     mid = (left + right) // 2
#     a2 = s(arr2[left:mid], arr2[mid:right])
#     return cmm(a1, a2)

# def merSort(array):
#     right=len(array)
#     left=0
#     mid=(left+right)//2
#
#     return s(array[left:mid], array[mid:right])
#
#     print(left, mid, right)
#     if left+1>=right:
#         return cmm(array)
#     else:
#         ll=merSort(array[left:mid])
#         print(ll)
#         lr=merSort(array[mid:right])
#         print(lr)
#     return ll+lr

# if __name__ == '__main__':
#     array=[3,5,2,1,7,6]
#     print(merSort(array))

# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     # def FindNumsAppearOnce(self, array):
#     #     sortArray=sorted(array)
#     #     ll=[]
#     #     while i <len(sortArray):
#     #         if sortArray[1+1]==sortArray[i]:
#     #             i+=2
#     #         else:
#     #             ll.append(sortArray[i])
#     #         if len(ll)=2:
#     #             return ll
#     def FindNumsAppearOnce(self, array):
#         sortArray=sorted(array)
#         ll=[]
#         i = 0
#         b=len(sortArray)
#         # print(sortArray)
#         while i <b-1:
#             # print(i,sortArray[i])
#             if sortArray[i+1]==sortArray[i]:
#                 i+=2
#             else:
#                 ll.append(sortArray[i])
#                 i+=1
#         if i==b-1:
#             ll.append(sortArray[i])
#         return ll

# if __name__ == '__main__':
#     l=[1,4,2,4,9,2]
#     print(Solution().FindNumsAppearOnce(l))


# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import re


# class Solution:
#     # s字符串
#     def isNumeric(self, s):
#         # write code here
#         return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)

# 按之字形顺序打印二叉树  todo
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def Print(self, pRoot):
# write code here


# -*- coding:utf-8 -*-
# hours = [9,9,6,0,6,6,9]
# score=[1, 1, -1, -1, -1, -1, 1]
# presum=[0,1,2, 1, 0, -1, -2, -1]
# stack=[0,5,6]
class Solution:
    def longestWPI(self, hours):  # todo 这一行有什么问题？
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
        # 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans = 0
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(n + 1):  # todo 为什么是n+1？
            if not stack or presum[stack[-1]] > presum[i]:
                stack.append(i)
        print(stack)
        # 倒序扫描数组，求最大长度坡  #todo ??
        i = n  # n=7
        while i > ans:
            while stack and presum[stack[-1]] < presum[i]:
                ans = max(ans, i - stack[-1])  # todo 为啥后面的栈不比了？
                stack.pop()
            i -= 1
        return ans


if __name__ == '__main__':
    print(Solution().longestWPI([9, 9, 6, 0, 6, 6, 9]))
