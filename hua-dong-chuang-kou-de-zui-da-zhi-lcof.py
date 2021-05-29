# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/  # todo 再做一遍
# 设数组 numsnums 的长度为 nn ，则共有 (n-k+1)(n−k+1) 个窗口
from nltk import collections


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):  # todo 是否可以写成左边界为（0，n-1）,有边界为（k-1,n+k-1）
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()  # 删除 deque 中对应的 nums[i-1]
            while deque and deque[-1] < nums[j]:
                deque.pop()  # 保持 deque 递减
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])  # 记录窗口最大值
        return res

    def maxSlidingWindow1(self, nums, k: int):
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]:  # 从右向左比较，每次弹出deque里面比当前数字小的
                deque.pop()
            deque.append(nums[i])  # 一开始dequeue中保存的是最大的
            print("nums[i],deque----", nums[i], deque)


        res = [deque[0]]
        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]:   #  从第2轮开始，需要注意第0个数是否在3个数的范围内如果deque的第0个数是第3个，pop
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
            print("nums[i],deque----",nums[i],deque)
        print("res---",res)
        return res
#dequeue为啥是递减？ -----因为要找的是最大的数
    def maxSlidingWindow2(self, nums, k: int):
        """
        和deque里面的数字从右往左比较，如果大于，则去掉当前的数；如果小于，就加到右边
        :param nums:
        :param k:
        :return:
        """
        l=len(nums)
        if l==0:
            return []
        d=collections.deque()
        d.append(nums[0])
        res=[]
        for i in range(1,k):
            while d and d[-1]<nums[i]:
                d.pop()
            d.append(nums[i])
        res.append(d[0])
        for i in range(k,l):
            if nums[i-k]==d[0]:
                d.popleft()
            while d and d[-1] < nums[i]:  # todo 为啥不能写while d[-1] and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
            res.append(d[0])
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    s.maxSlidingWindow1(nums=[3,1, -1, -3, 5, 3, 6, 7], k=3)
    print(s.maxSlidingWindow2(nums=[3,1, -1, -3, 5, 3, 6, 7], k=3))
