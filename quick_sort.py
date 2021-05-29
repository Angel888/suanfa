# O(n*(log n))


def quicksort(array):
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
        return quicksort(less) + [pivot] + quicksort(greater)
def quicksort1(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    less=[]
    more=[]
    for i in array[1:]:
        if i<pivot:
            less.append(i)
        else:
            more.append(i)
    return quicksort1(less)+[pivot]+quicksort1(more)
def bubble_sort(array):
    a_l=len(array)
    for i in range(a_l):
        tmp_min=array[i]
        for j in range(i+1,a_l):
            if array[j]<=tmp_min:
                tmp_min=array[j]
        array[i],tmp_min=tmp_min,array[i]
    return array

def bubbleSort(arr):
    """https://www.runoob.com/python3/python-bubble-sort.html"""
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
if __name__ == '__main__':
    print(bubbleSort(arr))

print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
# print(quicksort1([2, 5, 3, 3, 9, 7, 11]))
print(bubble_sort([2, 5, 3, 3, 9, 7, 11]))
# 这是一些测试样例
# print(quicksort([2, 5, 3,3, 9, 7, 11]))

# print(quicksort([152, 134, 38796, 7438415, 1, 2272, 34345, 24, 127]))
