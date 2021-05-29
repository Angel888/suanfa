# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
"""
https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


# 链接：https://leetcode - cn.com / problems / combination - sum / solution / hui - su - suan - fa - jian - zhi - python - dai - ma - java - dai - m - 2 /

    def combinationSum1(self, candidates: List[int], target: int):
        def dfs(candidates, target, combine, idx):
            if idx == self.l:
                return
            if target == 0:
                print("combine~~~~",combine)
                self.ans.append(combine[:])
                return
            if target < 0:
                return
            # if target-candidates[idx]>0:
            combine.append(candidates[idx])
            dfs(candidates, target - candidates[idx], combine, idx )
            combine.pop()
            dfs(candidates, target, combine, idx + 1)
        self.l=len(candidates)
        self.ans=[]
        dfs(candidates,target,[] ,0)
        print(self.ans)
        return self.ans

    def combinationSum2(self, candidates: List[int], target: int):
        def dfs(begin,candidates,target,path):
            if target==0:
                # print("path----",path)
                self.ans.append(path[:])
                return
            if target<0:
                return
            for i in range(begin,self.size):
                path.append(candidates[i])
                dfs(i,candidates,target-candidates[i],path)
                path.pop(-1)
        self.ans=[]
        self.size=len(candidates)
        if self.size == 0:
            return []
        dfs(0,candidates,target,[])
        return self.ans



if __name__ == '__main__':
    s=Solution()
    s.combinationSum(candidates = [2,3,6,7], target = 7)
    # s.combinationSum1(candidates = [2,3,6,7], target = 7)
    s.combinationSum2(candidates = [2,3,6,7], target = 7)