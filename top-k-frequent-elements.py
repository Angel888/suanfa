from nltk import collections


class Solution:
    def topKFrequent(self, nums, k) :
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root] # 用类似插入排序的赋值交换
            while root<<1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):  # child =len(heap)-1  #todo 没看懂是怎么上浮的？？
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            print("arr---",arr, "child---",child,"arr[child]---",arr[child])  # arr--- [(0, 0), (1, 3)] child--- 1
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val

        stat = collections.Counter(nums)
        # print("stat--",stat)
        # print("stat.items()-----",stat.items())
        stat = list(stat.items())
        # print("stat--", stat) #stat-- [(1, 3), (2, 2), (3, 1)]
        heap = [(0,0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap)-1)
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1)
        return [item[0] for item in heap[1:]]
if __name__ == '__main__':
    s=Solution()
    s.topKFrequent(nums = [1, 1, 1, 2, 2, 3], k = 2)