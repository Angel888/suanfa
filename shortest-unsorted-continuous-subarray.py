# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
class Solution:
    # todo 为什么要从左边找右边界，从右边找左边界？
    def findUnsortedSubarray(self, nums) -> int:
        l_n=len(nums)
        max_n= nums[0]
        min_n=nums[-1]
        begin,end=0,-1  # 这里的end必须得是-1!!!
        for i in range(l_n):
            if nums[i]<max_n:
                end=i  # 如果右边的数比左边的大，那么右边界得再往右
            else:
                max_n=nums[i]
            if nums[l_n-i-1]>min_n:
                begin=l_n-i-1 # 如果右边的数比左边的大，那么右边界得再往右
            else:
                min_n=nums[l_n-i-1]
        short_len=end-begin+1
        print(short_len)
        return short_len
if __name__ == '__main__':
    s=Solution()
    # s.findUnsortedSubarray(nums = [2,6,4,8,10,9,15])
    # s.findUnsortedSubarray(nums = [1,2,3,4])
    # s.findUnsortedSubarray(nums = [2,1,4,3])
    # s.findUnsortedSubarray(nums = [1])
    s.findUnsortedSubarray(nums = [1,2,3,3,3])
