# 输入：m = 2, n = 3, k = 1  #todo  深度优先和广度优先各做一遍
# 输出：3
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        每遍历一个点都记到visited
        si + sj 为数位和
        个位或者10位增加1，可以有数位增量的计算公式
        """

        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
                                                                                   sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount1(self, m: int, n: int, k: int) -> int:
        """
        每当把一个值推出栈时，只要根据它变化的值符合条件，则加到栈里面
        """

        queue, visited,  = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i,j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)



def digit_sum(a):
    res = 0
    while a > 0:
        b = a % 10
        res += b
        a = (a - b) / 10  # 可以写成a=a//10
    return res


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(m = 2, n = 3, k = 1))
