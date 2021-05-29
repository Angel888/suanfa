# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

class Solution:
    def translateNum(self, num):
        a=[1,1]
        l=len(num)
        # print("l",l)
        for i in range(2,l+1):
            if 9<int(num[i-2]+num[i-1])<26:  #todo 这个两位数怎么写？
                a.append(a[i-1]+a[i-2])
            else:
                a.append(a[i - 1])
        # print(a)
        return a[-1]

    def translateNum1(self, num: int) :
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a


if __name__ == '__main__':
    s=Solution()
    print(s.translateNum("12345"))
    print(s.translateNum("12258"))
    print(s.translateNum1("12345"))


