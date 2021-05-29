# https://leetcode-cn.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int):
        self.res = []
        self.k = k

        def dfs(begin, com):
            if len(com) == self.k:
                #print(com[:])
                self.res.append(com[:])
                return
            elif len(com) < k:
                for i in range(begin, n):
                    com.append(i + 1)
                    dfs(i+1, com)
                    com.pop(-1)
                return

        dfs(0, [])
        #print("self.res---",self.res)
        return self.res

    def combine1(self, n: int, k: int) :  #todo 怎么剪枝没看

        all_combination = []

        def backtracking(remain_selection, unfinished_count, prefix):
            if unfinished_count == 0:
                all_combination.append(prefix[:])
            tmp_length = len(remain_selection)
            for i in range(tmp_length):
                # 此处代码优化可以显著提高运行的效率
                if unfinished_count <= tmp_length - i + 1:
                    backtracking(remain_selection[i + 1:], unfinished_count - 1, prefix + [remain_selection[i]])
                else:
                    break

        if n < k or n <= 0 or k <= 0:
            return []
        backtracking([i for i in range(1, n + 1)], k, [])
        return all_combination
if __name__ == '__main__':
    s = Solution()
    s.combine(n=4, k=2)
