# https://leetcode-cn.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums, target):
        sorted_nums = sorted(nums)
        b = len(sorted_nums)
        act_sum=sum([sorted_nums[0], sorted_nums[1], sorted_nums[2]])
        start_gap = act_sum-target
        if start_gap==0:
            return act_sum
        for i in range(b):
            start = i + 1
            end = b - 1
            while start < end:
                sum_find = sum([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                gap = sum_find - target
                # if gap > 0 and abs(gap) <= abs(start_gap):
                #     start_gap = gap
                #     act_sum = sum_find
                #     end = end-1
                # elif gap < 0 and abs(gap) <= abs(start_gap):
                #     start_gap = gap
                #     act_sum = sum_find
                #     start = start+1
                # elif gap==0:
                #     act_sum=sum_find
                #     return act_sum
                # else:
                #     break
                if abs(gap) <= abs(start_gap):
                    start_gap = gap
                    act_sum = sum_find
                if gap > 0:
                    end = end - 1
                elif gap<0:
                    start = start + 1
                else:
                    act_sum=sum_find
                    return act_sum
        return act_sum


if __name__ == '__main__':
    # print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    # print(Solution().threeSumClosest([1,1,1,0], 1))
    print(Solution().threeSumClosest([1,2,4,8,16,32,64,128], 82))
