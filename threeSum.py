class Solution:  #todo 重新做一遍三数之和
    def threeSum(self, nums):
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            second = i + 1
            third = l - 1  # todo为啥third不也从左边开始
            while second < third:
                if nums[second] + nums[third] < target:
                    second += 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                elif nums[second] + nums[third] > target:
                    third -= 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                else:
                    res.append([nums[i], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res
if __name__ == '__main__':
    s=Solution()
    print(s.threeSum([-2,0,1,1,2]))