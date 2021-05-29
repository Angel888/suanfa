class Solution:
    def validateStackSequences(self, pushed, popped):
        # a=[]
        # i=0
        # while popped:
        #     while pushed[i]!=popped[0]:
        #         i+=1
        #     while pushed[i]==popped[0]:
        #         popped.pop(0)
        #         i-=1
        pass

    def validateStackSequences1(self, pushed, popped):
        # while popped and pushed:
        #     i=0
        #     while pushed[i]!=popped[0]:
        #         i+=1
        #     while  pushed[i]==popped[0]:
        #         pushed.pop(i)
        #         popped.pop(0)
        #         i+=1
        # while pushed[i] != popped[0]:
        #     a.append(pushed[i])
        #     i+=1
        # while a[-1]==popped[0]:
        #     a.pop(-1)
        #     popped.pop(0)
        # while pushed[i]==popped[0]:
        #     popped.pop(0)
        #     i+=1
        a = []
        i = 0
        push_l=len(pushed)
        while len(popped) > 0 and (len(a) > 0 or i < push_l):
            if i<push_l and pushed[i] != popped[0]:
                if len(a) > 0 and a[-1] == popped[0]:
                    a.pop(-1)
                    popped.pop(0)
                else:
                    a.append(pushed[i])
                    i += 1
            elif i<push_l and pushed[i] == popped[0] :
                popped.pop(0)
                i += 1
            elif i >= push_l and len(a)>0 and a[-1]!= popped[0]:
                return False
            elif i >= push_l and len(a)>0 and a[-1]== popped[0]:
                a.pop(-1)
                popped.pop(0)

        if len(popped) == 0 and len(a) == 0:
            return True
        else:
            return False

    def validateStackSequences2(self, pushed, popped):
        st=[]
        for i in pushed:
            st.append(i)
            while st[-1]==popped[0]:
                st.pop(-1)
                popped.pop(0)
        if len(st)>0:
            return False
        return True



# todo 是否可以没有a这个变量
if __name__ == '__main__':
    # pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
    # pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1] True
    s = Solution()
    print(s.validateStackSequences1([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.validateStackSequences1([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
