class Solution:
    def simplify_path(self,str):
        str_list=str.split("/")
        act_path=[]
        n=0
        for i in str_list:
            if i=="..":
                n-=1
            elif i==".":
                pass
            else:
                act_path.append(i)
        ret=act_path[n] if len(act_path)>n else "/"
        print(ret)
        return ret
if __name__ == '__main__':
        Solution().simplify_path("/home/")