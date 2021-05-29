class Solution:
    def firstUniqChar(self, s: str):
        m={}
        for i in s:
            if i not in m :
                m[i]=True
            else:
                m[i]=False
        for i in s:
            if m[i]:
                return i
        return ""
