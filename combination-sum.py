# todo
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
class Solution:
    def combinationSum(self, candidates, target: int):
        """
        使用动态规划
        1 从小到大遍历target
        1 遍历数组，直到>target,
        2 每到一个数i，找到target-i对应的解集
        :param candidates:
        :param target:
        :return:
        """
        candidates.sort()
        l = len(candidates)
        sub_sum = {}
        for i in range(1,target + 1):
            v_combine=set()
            for j in range(l):  # 在数组中寻找和为i的数字
                if candidates[j] > i:
                    break
                elif candidates[j] == i:
                    s=set()
                    s.add(candidates[j])
                    v_combine.add(s)
                else:
                    p=i-candidates[j]
                    if p in sub_sum.keys():
                        for b in sub_sum[p]:  # odo 这两行为什么不能写到一起？
                            # if i == 4:
                            #     print("[j]---",[j])
                            # print("[candidates[j]],[b]---",[candidates[j]],b)
                            # print("[candidates[j]]+[b]---",)
                            s = set()
                            s.add(candidates[j])
                            s.add(b)
                            if s not in v_combine:
                                v_combine.add(s)

            if len(v_combine)>0:
                sub_sum[i]=v_combine
        print(sub_sum)
        return sub_sum.get(target,-1)

    def combinationSum1(self, candidates, target: int):
        """
        使用dfs+回溯
        dfs逻辑：输入为target、
        """
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








if __name__ == '__main__':
    s = Solution()
    s.combinationSum(candidates=[2, 3, 6, 7], target=7)
