class Solution:
    from typing import List
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left
    def findDuplicate1(self, nums: List[int]) -> int:
        fast,slow=0,0
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
        finder=0

if __name__ == '__main__':
    s=Solution()
    s.findDuplicate(nums = [3,1,3,4,2])