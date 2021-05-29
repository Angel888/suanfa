# https://leetcode-cn.com/problems/longest-well-performing-interval/
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 请你返回「表现良好时间段」的最大长度。

# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。

arr = [1, 1, -1, -1, -1, -1, 1]
prefixSum = []  # 前缀和数组

cur_sum = 0
for val in arr:
    prefixSum.append(cur_sum)
    cur_sum += val
prefixSum.append(cur_sum)

print(prefixSum)  # [0, 1, 2, 1, 0, -1, -2, -1] 注意这里比arr多了一个元素

# a    [1, 1, -1, -1, -1, -1, 1]
# b [0, 1, 2, 1, 0, -1, -2, -1]

class Solution:
    def longestWPI(self, hours):
        l=len(hours)
        # print("l--",l)
        a=[]
        b=[]
        for i in hours:
            if i >8:
                a.append(1)
            else:
                a.append(-1)
        # print("!",a)
        b.append(0)
        c=[]
        for i in range(l):
            b.append(a[i]+b[i])   # b是前缀和，也就是从第0个开始，到这一天，劳累的天数-不劳累的天数的天数
        # print("@@",b)   # todo 找出b中 间隔最大，而且后面-前面>0的数  b=[0, 1, 2, 1, 0, -1, -2, -1]
        # [0,-1,-2]  #从前到后，找出严格递减的数 [0,5,6]
        # [2,0,-1]  # 从后到前，找出严格递增的数 [2,4,5]
        res=0
        for i in range(l,-1,-1):
            for j in range(i):
                if b[i]-b[j]>0:
                    res=max(i-j,res)
                    continue
        # print("~~~~~~",res)
        return res
    def longestWPI1(self, hours) :
        """
        arr是1和-1的列表
        prefixSum是arr的前缀和
        :param hours:
        :return:
        """
        arr = []
        for val in hours:
            if val > 8:
                arr.append(1)
            else:
                arr.append(-1)

        prefixSum = []  # 前缀和数组
        cur_sum = 0
        for val in arr:
            prefixSum.append(cur_sum)
            cur_sum += val
        prefixSum.append(cur_sum)
        print("prefixSum~~~~~",prefixSum)
        stk = []
        for i in range(len(prefixSum)):
            if len(stk) == 0 or prefixSum[stk[-1]] > prefixSum[i]:   #todo 这里不太理解
                print("stk,i*****",stk,i)
                stk.append(i)  # 因为最终需要的答案是最长距离,需要下标来计算,所以这里存储下标
        print("stk----",stk)   # stk为[0, 1, 2]
        res = 0
        # 逆向遍历prefixSum
        for j in range(len(prefixSum) - 1, -1, -1):
            # 成立的话, (stk[-1], j)是一个候选项
            while len(stk) != 0 and prefixSum[j] > prefixSum[stk[-1]]:
                res = max(res, j - stk[-1])
                stk.pop()
        print("res--",res)
        return res
# 假设要找的数是i和j
#作为i，



if __name__ == '__main__':
    # Solution().longestWPI([9, 9, 6, 0, 6, 6, 9])
    # Solution().longestWPI1([9, 9, 6, 0, 6, 6, 9])
    # Solution().longestWPI([6,6,9])  # [-1,-1,1]  #[0,-1,-2，-1]
    Solution().longestWPI1([6,6,9])
