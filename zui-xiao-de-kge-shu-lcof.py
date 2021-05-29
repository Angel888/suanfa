# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
import heapq
import random


class Solution1:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:  # 从左向右遍历，如果左边的<=r,则
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):  #
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr, k: int) :
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]
class Solution:
    def fast_sort(self,li):
        p=0
        l=p+1
        l=len(li)
        r=l-1
        for i in range(l,r):
            if li[l]<li[p]:
                l+=1
        r+=1



