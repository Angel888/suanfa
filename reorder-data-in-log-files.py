# https://leetcode-cn.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs) :  #todo 不是自己做的
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l1=[]
        l2=[]
        for l in logs:
            if l[-1].isalpha():
                l1.append(l)
            else:
                l2.append(l)
        print(l1)  #['g1 act car', 'ab1 off key dog', 'a8 act zoo']
        l1.sort(key=lambda x:(x[x.index(' ')+1:],x[:x.index(' ')]))
        return l1+l2
if __name__ == '__main__':
    logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Solution().reorderLogFiles(logs)