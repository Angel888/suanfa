# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target: int):
        hashtable = dict()
        for i, num in enumerate(nums):
            print("!!!!!",hashtable)
            if target - num in hashtable:
                print("~~~~~",hashtable)
                print("---",hashtable[target - num],i)
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    Solution().twoSum(nums=[2, 7, 11, 15], target=9)
