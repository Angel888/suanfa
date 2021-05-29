# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
class Solution:
    def exchange(self, nums):
        l = len(nums)
        i = 0
        j = l - 1
        while i<j :
            while -1<i<l and nums[i] % 2 == 1 :
                i += 1
            while -1<j<l and nums[j] % 2 == 0 :
                j -= 1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        return nums
if __name__ == '__main__':
    s=Solution()
    print(s.exchange([1,2,3,4]))
    print(s.exchange([1,3,5]))
    # print(s.exchange([1,11,14]))