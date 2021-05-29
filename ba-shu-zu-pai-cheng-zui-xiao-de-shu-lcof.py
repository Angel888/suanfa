# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# 输入: [10,2]
# 输出: "102"

# 输入: [3,30,34,5,9]
# 输出: "3033459"

# x + y > y + x   则 m > n
# 即要把x放左边
# eg:"330">"303"  则"30"<"3"

class Solution:
    def minNumber(self, nums):
        """
        先对数组进行排序，如果最小的是0，那么把第二位放到最左边
        :param nums:
        :return:返回一个字符串
        """
        sorted(nums)
        a=len(nums)
        for i in range(a):
            if nums[i]==0:
                i+=1
            else:
                break
        a=[]
        a.append(nums[i])
        a.extend(nums[:i])
        a.extend(nums[i + 1:])
        str1="".join(str(k) for k in a)
        # print("str1",str1)
        return str1

    def minNumber1(self, nums):
        """
        要找到最高位最小的
        :param nums:
        :return:
        """
        one_p=[]
        while nums:
            nums.sort(key=lambda x:int(str(x)[0]))  # todo 第一位和第二位一样的话怎么搞？？

    def minNumber2(self, nums):
        """
        :param nums:
        :return:
        """
        def fast_sort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
                strs[i], strs[j] = strs[j], strs[i]  # todo ？
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)

        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)







if __name__ == '__main__':
    Solution().minNumber([10,2])
    Solution().minNumber([3,30,34,5,9])  # 3033459"

