class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        length = len(tasks)
        if length <= 1:
            return length
        if n==0:
            return length

        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)  # lambda的使用！！# sorted不一定非要传列表，
        # for item in a.items()中的每一个item都是一个元组
        print("task_sort---", task_sort)
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:  # task_sort任务的最后一个也要算到里面
            if sort[1] == max_task_count:
                res += 1

        # 如果结果比任务数量少，则返回总任务数
        print("res---",res)
        print("length---",length)
        # return res if res >= length else length   # todo 否存在res<length的情况？为什么要返回大的？因为即使所有的任务不间断进行，也得length时间才能完成。res计算了包括冷却时间在内的最短时间
        return res


def build(x, y):
    return lambda: x * x + y * y


if __name__ == '__main__':
    a = {1: 2, 3: 8, 5: 6}
    s = Solution()
    # s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2)
    # s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0)
    # s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)
    s.leastInterval(tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],n=2)
