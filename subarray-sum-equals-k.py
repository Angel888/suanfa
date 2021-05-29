# https://leetcode-cn.com/problems/subarray-sum-equals-k/ 和为k的子数组
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # a=0
        l=len(nums)
        print(nums)
        res=[]
        for a in range(l):
            sum_k=nums[a]
            for b in range(a+1,l+1):
                # print(a,b,sum_k)
                if sum_k == k:
                    res.append(nums[a:b])
                if b<l:
                    sum_k += nums[b]
                    b+=1

        # print(res)
        return len(res)

    def subarraySum1(self, nums, k: int) -> int:
        """
        维护一个前缀和的哈希表，遍历到某个值a时，看表中前缀和为k-a的个数
        :param nums:
        :param k:
        :return:
        """
        pre_num={}
        count=0
        tmp_sum=0
        for i in nums:
            tmp_sum+=i
            b=pre_num.get(tmp_sum,0)
            pre_num[tmp_sum]=b+1
            # todo todo为啥不能这样写？
            # pre_num[tmp_sum]=pre_num.get(tmp_sum,0)+1
            a = tmp_sum - k
            if a in pre_num.keys():
                count+=pre_num[a]
        print(count)
        return count
    def subarraySum2(self, nums, k: int) -> int:
        """
        维护一个前缀和的哈希表，遍历到某个值a时，看表中前缀和为k-a的个数
        :param nums:
        :param k:
        :return:
        """
        pre_num={0:1}
        count=0
        tmp_sum=0
        for i in nums:
            tmp_sum+=i
            # if tmp_sum==k:  # todo 为什么这种情况要单独写出来？因为还有前0项和为0的没表示
            #     count+=1
            a=tmp_sum-k
            if a in pre_num.keys():
                count+=pre_num[a]
            pre_num[tmp_sum]=pre_num.get(tmp_sum,0)+1
        # print(pre_num)
        # print(count)
        return count

if __name__ == '__main__':
    s=Solution()
    # s.subarraySum(nums = [1,1,1], k = 2)
    s.subarraySum2(nums = [1,1,1], k = 2)
    # s.subarraySum([1,2,3],3)
    # s.subarraySum([-1,0,1],0)
    # s.subarraySum2([1,-1,0],0) # 前缀和：[1,0,0]