class Solution:
    def isValid(self, s: str) -> bool:
        a = { ')':'(',  '}':'{',  ']':'['}
        a_k=['(','{','[']
        m = {}
        for i in s:
            if i in a_k:  # 当为左括号时
                m[i]=m.get(i, 0) + 1
            # print("----i",i, "a.values()", a.values(),"type(a.values())",type(a.values()))
            else:
                # print("----", m.get(a[i], 0))
                if m.get(a[i], 0) <= 0:  # 当为右括号时
                    # print("sss")
                    return False
                if m.get(a[i], 0) > 0:
                    m[a[i]] -= 1
        for i in m:
            if m[i] != 0:
                return False
        return True

    def isValid1(self, s: str) -> bool:
        stk=[]
        a = {')': '(', '}': '{', ']': '['}
        a_k = ['(', '{', '[']
        for i in s:
            # print("stk--",stk)
            if i in a_k:
                # print(1)
                stk.append(i)
            else:
                # print(stk[-1],"--",a[i])
                if stk and stk[-1]==a[i]:
                    # print(2)
                    stk.pop(-1)
                else:
                    # print(3)
                    return False
        if not stk:
            # print(4)
            return True

if __name__ == '__main__':
    s = "()[]{}"
    a = Solution()
    a.isValid1(s)
    # a.isValid1("(]")
    # a.isValid1("()")
