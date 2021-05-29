# 每日温度
# https://leetcode-cn.com/problems/daily-temperatures/  todo 自己写一下用栈的方式
# 要想观测到更高气温，至少需要等待的天数
# 给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

# 寻找第一个比它大的元素的相对位置
# 方法一：使用栈，没找到更大的数,则记录在栈中；找到了就从栈中去掉
# 应该有两种使用栈的方式。一种是用栈来存储没找到后面值的数；一种是用栈来存储

# 方法二 :从后面开始遍历，；利用已经获得的后面的值，减少时间复杂度
class Solution:
    def dailyTemperatures(self, T):
        l=len(T)
        res=[0]*l
        stk=[]
        stk.append(0)
        for i in range(1,l):
            print(i,stk[-1])
            while len(stk)>0 and T[i]>T[stk[-1]]:
                res[stk[-1]] =i-stk[-1]
                stk.pop()
            stk.append(i)
        # print(res)
        return res


    def dailyTemperatures1(self, T):
        """
        遍历T,当T[i]的值大于栈顶的值，将栈顶的值去掉，并求栈中这个值和T[i]的相对位置，加到ans；
        如果T[i]的值小于栈顶的值，则加入栈中
        qustion:为啥用栈而不是列表？栈的存在有什么作用？
        answer:栈顶每次会记录当前遇到最大的值。整个栈记录的是遍历到当前位置时，存在的后面没有比大的数
        初步思考：
        question:ans是做啥的？prev_index又是做啥的?stack又是做啥的？
        answer:ans是最终的结果 prev_index是栈顶的元素，也就是当前出现的最大的值
        如果比栈顶元素小，则移动到栈;如果比栈顶元素大，则从栈顶依次移除大的，再进栈
        出栈是stack.pop(),进栈是append()    ans的赋值方式为 i时给i-1赋值
        只需要和栈顶比较一下就可以了吗？栈顶的数一定是最大的吗？
        是的，因为只要遇到比栈顶更大的，就会出栈；只有比栈顶小的，才会被加到栈里面
        """
        length = len(T)
        ans = [0] * length
        stack = []  #
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:  # 栈
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

    def dailyTemperatures2(self, T):
        """
        # 为啥要从后面开始遍历？

        :param T:
        :return:
        """
        n = len(T)
        # print(n)  #8
        ans = [0] * n
        for i in range(n - 2, -1, -1):  # (6,-1,-1)
            now = i + 1
            while T[now] <= T[i]:  # now是它后面的数
                if ans[now]:
                    # print("ans---", ans)
                    # print("i,now,ans[now]-----", i, now, ans[now])
                    now += ans[now]  # now=now+ans[now]
                    # print("新now---", now, "\n")
                else:
                    break
            else:
                ans[i] = now - i
        print(ans)
        return ans
    def dailyTemperatures3(self, T):
        """
        如果有栈，则j的数先和栈中的数进行比较
        如果没有栈，和i比较
        :param T:
        :return:
        """
        a=len(T)
        stack=[]
        ans=[0]*a
        for i in range(a):  # 每次不是找i的ans值，而是通过i来找前面的ans todo 为啥和后面的数比较不行？
            temp=T[stack[-1]]
            while stack and T[stack[-1]]<temp:
                s=stack.pop()
                ans[s]=a-s
            stack.append(i)
        return ans

    def dailyTemperatures4(self, T):
        """
        倒序比较
        :param T:
        :return:
        """
        a=len(T)
        ans=[0]*a
        for i in range(a-2,-1,-1):
            j=i+1
            if T[i]<T[j]:
                ans[i]=1
            else:
                for p in range(j,a-1):
                    print(p+ans[p])
                    if T[p+ans[p]]>T[i]:
                        ans[i]=p+ans[p]
                        break
                ans[j]=0
        # print(ans)
        return ans






if __name__ == '__main__':
    Solution().dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73])  # 长度为8
    Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])  # 长度为8

