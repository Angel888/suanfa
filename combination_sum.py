# https://leetcode-cn.com/problems/combination-sum/
# https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
from typing import List


# 说明：
#
# 以 target = 7 为 根结点 ，创建一个分支的时 做减法 ；
# 每一个箭头表示：从父亲结点的数值减去边上的数值，得到孩子结点的数值。边的值就是题目中给出的 candidate 数组的每个元素的值；
# 减到 00 或者负数的时候停止，即：结点 00 和负数结点成为叶子结点；
# 所有从根结点到结点 00 的路径（只能从上往下，没有回路）就是题目要找的一个结果。
# 这棵树有 44 个叶子结点的值 00，对应的路径列表是 [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]，而示例中给出的输出只有 [[7], [2, 2, 3]]。即：题目中要求每一个符合要求的解是 不计算顺序 的。下面我们分析为什么会产生重复。
#
# 针对具体例子分析重复路径产生的原因（难点）
# 友情提示：这一部分我的描述是晦涩难懂的，建议大家先自己观察出现重复的原因，进而思考如何解决。
#
# 产生重复的原因是：在每一个结点，做减法，展开分支的时候，由于题目中说 每一个元素可以重复使用，我们考虑了 所有的 候选数，因此出现了重复的列表。
#
# 一种简单的去重方案是借助哈希表的天然去重的功能，但实际操作一下，就会发现并没有那么容易。
#
# 可不可以在搜索的时候就去重呢？答案是可以的。遇到这一类相同元素不计算顺序的问题，我们在搜索的时候就需要 按某种顺序搜索。具体的做法是：每一次搜索的时候设置 下一轮搜索的起点 begin，请看下图。
#

class Solution1:
    def combinationSum(self, candidates: List[int], target: int):

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                # print(index)
                print(path)
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        print(res)
        return res
# 手动写的思路：
# begin=0,size=4
# dfs(candidates,0,4,[],[],7)
# target>0
# for index in (0,4):
#     index=0,dfs(candidates,0,4,[2],[],5) ->dfs(candidates,0,4,[2,2],3)->dfs(candidates,0,4,[2,2,2],1),dfs(candidates,0,4,[2,2,3],1)
#
#       dfs(candidates,0,4，
    def combinationSum1(self,candidates, target):

        def get_val(candidates,begin,l,path,target,res):
            if target<0 :
                return
            elif target==0:
                res.append(path)
                return
            else:
                for i in range(begin,l):
                    get_val(candidates,i,l,path+[candidates[i]],target-candidates[i],res)

        path = []
        res = []
        begin=0
        l=len(candidates)
        target=target
        get_val(candidates,begin,l,path,target,res)
        print(res)
#         todo  res可以不传吗？ begin是什么？
#
#

# from typing import List
#
#
# class Solution:
#     def combinationSum3(self, candidates: List[int], target: int) :
#
#         def dfs(candidates, begin, size, path, res, target):
#             if target < 0:
#                 return
#             if target == 0:
#                 res.append(path)
#                 return
#
#             for index in range(begin, size):
#                 dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])
#
#         size = len(candidates)
#         if size == 0:
#             return []
#         path = []
#         res = []
#         dfs(candidates, 0, size, path, res, target)
#         return res



if __name__ == '__main__':
    Solution1().combinationSum1([2, 3, 6, 7], 7)
