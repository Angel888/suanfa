class Solution:
    def verifyPostorder(self, postorder):
        l = len(postorder)
        if l < 2:
            return True
        node = postorder[-1]
        a = l - 1
        i = 0
        while postorder[i] < node and i < l-1:
            i += 1
        b = i
        # print("b",b)
        # if b == a or b == 0:
        #     return True
        for i in range(b, a):
            if postorder[i] < node:
                return False
            # print("a,b",a,b)
        r_1 = self.verifyPostorder(postorder[:b])
        if b<a-1:
            r_2 = self.verifyPostorder(postorder[b:a])
        else:
            r_2=True
        print(b,r_1,r_2)
        if r_1 is False or r_2 is False:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.verifyPostorder([3,10,6,9,2]))
    print(s.verifyPostorder([1,6,3,2,5]))
    print(s.verifyPostorder([1, 3, 2, 6, 5]))
    print(s.verifyPostorder([4, 8, 6, 12, 16, 14, 10]))
    print(s.verifyPostorder([1, 2, 3, 4, 5]))
    print(s.verifyPostorder([7, 4, 6, 5]))
