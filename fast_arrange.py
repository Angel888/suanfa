l = [3, 7, 6, 2, 5, 1]


class Solution:
    def fast_arrange(self, l):
        c = len(l)
        a = 1
        b = c - 1
        i, j = a, b
        if i >= j:
            return l
        mid = l[i]
        while i < j:
            while l[i] < mid and i < j:
                j -= j
                print(j)
            l[j], mid = mid, l[i]
            while mid < l[j] and i < j:
                i += i
                print(i)

            l[i], mid = mid, l[i]
            self.fast_arrange(l[0, ])
            self.fast_arrange(l[i + 1, b])

    def quicksort(self, array):  # 这个快排是什么含义？？
        if len(array) < 2:
            return array
        else:
            pivot = array[0]  # 找到一个基准值
            # 遍历整个列表，将小于这个基准值的元素放到一个子列表中
            less = [i for i in array[1:] if i < pivot]
            # 遍历整个列表，将大于这个基准值的元素放到一个子列表中
            greater = [i for i in array[1:] if i > pivot]
            # 首先，明确我们对元素为0个/1个的列表无需要排序
            # 使用函数递归
            # 目标：让我们在一个基准值的一侧变为有序，然后依次返回，让我们的每个基准值的两侧都变得有序
            return self.quicksort(less) + [pivot] + self.quicksort(greater)


# 这是一些测试样例
if __name__ == '__main__':
    s = Solution()
    # print(s.quicksort([2,5,3,9,7,11]))
    print(s.fast_arrange([2, 5, 3, 9, 7, 11]))
    # print(s.quicksort([152,134,38796,7438415,1,2272,34345,24,127]))
