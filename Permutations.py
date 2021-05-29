# https://leetcode-cn.com/problems/permutations/
# https://leetcode-cn.com/problems/permutations/submissions/ todo
    # 输入: [1,2,3]
    # 输出:
    # [
    #   [1,2,3],
    #   [1,3,2],
    #   [2,1,3],
    #   [2,3,1],
    #   [3,1,2],
    #   [3,2,1]
    # ]
    #
# 方法一：每次固定开头的字母，交换后面的
class Solution:
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res=[]
    #     n=len(nums)
    #     for i in range(n):
    #
    #         self.back_track(i,n,nums)
    # def back_track(self,i,n,nums):
    #     for j in range(i,n):
    #         if

    # 定义递归函数 backtrack(first, output) 表示从左往右填到第 \textit{first}first 个位置
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #
    #     def backtrack(first=0):
    #         # 所有数都填完了
    #         if first == n:
    #             res.append(nums[:])
    #         for i in range(first, n):
    #             # 动态维护数组
    #             nums[first], nums[i] = nums[i], nums[first]
    #             # 继续递归填下一个数
    #             backtrack(first + 1)
    #             # 撤销操作
    #             nums[first], nums[i] = nums[i], nums[first]
    #
    #     n = len(nums)
    #     res = []
    #     backtrack()
    #     print(res)
    #     return res

    def permute(self, nums):
        res=[]
        n = len(nums)
        self.back_track(0,nums,res,n)
        print(res)
    def back_track(self,first,n,r,l):
        if first==l:
             r.append(n[:])
        for i in range(first,l):
            n[first],n[i]=n[i],n[first]
            self.back_track(first+1,n,r,l)
            # self.back_track(i+1,n,r,l)
            n[first],n[i]=n[i],n[first]



class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 遍历数组
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                print("nums---",nums)
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

    def permute1(self, nums):
        def dfs(first=0):
            if first==l:
                print(nums, nums[:])
                self.res.append(nums[:])
            for i in range(first,l):
                nums[first],nums[i]=nums[i],nums[first]
                dfs(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        self.res=[]
        l=len(nums)
        dfs()
        print(self.res)
        return self.res

if __name__ == '__main__':
    Solution1().permute1([1,2,3])