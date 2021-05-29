class Solution:
    from typing import List

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero = 0
        two = size

        i = 0

        while i < two:  # two为nums的长度，zero为最后一个0的位置遍历这个数组，如果为0，
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(nums, i, two)

    def sortColors1(self, nums: List[int]) -> None:
        l_n = len(nums)
        i, left, right = 0, 0, l_n - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:  # 为啥为2时i不+1？因为替换后的数字还没有比！！！
                # print(right, i)
                nums[i], nums[right] = nums[right], nums[i]
                # print("--", i, right,nums)
                right -= 1
            else:
                i += 1
        # print(nums)
        return



if __name__ == '__main__':
    s = Solution()
    # s.sortColors1([2, 0, 2, 1, 1, 0])
    # s.sortColors1([2, 0, 1])
    # s.sortColors1([0])
    # s.sortColors1([1])
    s.sortColors1([1,2,0])
