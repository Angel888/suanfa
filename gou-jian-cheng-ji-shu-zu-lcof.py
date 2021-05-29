# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
# B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]
class Solution:  #todo 看了答案的思路做对的，可以再做一遍
    def constructArr(self, a):
        res = []
        l = len(a)
        for i in range(l):
            b = 1
            for j in range(l):
                if j == i:
                    continue
                else:
                    b = b * a[j]
            res.append(b)
        return res

    def constructArr1(self, a):
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b

    def constructArr2(self, a):
        l=len(a)
        tmp=1
        b=[1]*l
        for i in range(1,l):
            b[i]=b[i-1]*a[i-1]
        for j in range(l-2,-1,-1):
            tmp=tmp*a[j+1]
            b[j]=b[j]*tmp
        return b



if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1, 2, 3, 4, 5]))
    print(s.constructArr2([1, 2, 3, 4, 5]))
