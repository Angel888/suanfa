# https://leetcode-cn.com/problems/target-sum/
class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            print([num for num in res],i)
            res = res + [[i] + num for num in res]
        print(print("1",res))
        return res

    def subsets1(self, nums):
        # todo 没看懂回溯法
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

    def subsets2(self, nums) :
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                print(j , tmp ,nums[j])
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

    def subsets4(self, nums) :
        res=[[]]
        for i in nums:
            tmp=[]
            for j in res:
                tmp.append(j+[i])
            res+=tmp
        print("2",res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.subsets(nums=[1, 2, 3])
    # s.subsets2(nums=[1, 2, 3])
    s.subsets4(nums=[1, 2, 3])
