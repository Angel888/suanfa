import sys
class Solution:
    def reverseStringI(self , str ):
        sys.stdout.write("2222")
        str_l=str.split()
        for i,v in enumerate(str_l):
            # str_l[i]=list(v)[::-1]
            str_l[i]=v[::-1]
        res=" ".join(str_l)
        return res
if __name__ == '__main__':
    print(Solution().reverseStringI("i am a student"))