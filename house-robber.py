class Solution:
    def rob(self, nums) :
        res=[nums[0],nums[1]]
        l=len(nums)
        for i in range(2,l):
            res.append(max(res[i-1],res[i-2]+nums[i]))

        return res[-1]
if __name__ == '__main__':
    s=Solution()
    s.rob([2,7,9,3,1])
