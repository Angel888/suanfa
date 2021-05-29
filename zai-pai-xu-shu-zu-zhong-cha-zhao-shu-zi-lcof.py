class Solution:
    def search(self, nums, target) -> int:
        a = 0
        b = len(nums) - 1
        n = 0
        while a <= b:
            m = (a + b) // 2
            if m < target:
                a = m
            elif m > target:
                b = m
            else:
                i = m - 1
                n = 1
                while nums[i] == target:
                    n += 1
                    i -= 1
                j = m + 1
                while nums[j] == target:
                    n += 1
                    j += 1
                return n
        return n

    def search1(self, nums: [int], target: int) -> int:  #  先找到左边界，再找到右边界的方式
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1


if __name__ == '__main__':
    Solution().search1([5, 7, 7, 8, 8, 10], target=8)
    # 0+5=5 2,4
    #
