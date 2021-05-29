class Solution:
    def missingNumber(self, nums) -> int:
        """
        当[a,b]为空时，就找到了这个数，也就是当a,b,m对应的为一个值时，就可以终止循环了
        :param nums:
        :return:
        """
        a = 0
        b = len(nums) - 1
        # while a < b:
        while a != b:
        # while a <= b:  # todo 之所以写成<=而不是==的原因是：如果a==m,则=m+1会出界，则，这个时候就应该终止循环了
            # print(a,b)
            m = (a + b) // 2
            if nums[m] == m:
                a = m+1
            else:
                b = m
                # b=m-1 # todo  当刚好是第m位时，会跳出循环。当b(m-1)<a时，说明已经走过了a==b。
        if nums[a]==a:  #todo ????
            a+=1
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([0, 1, 3]))
    print(s.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
    print(s.missingNumber([0]))
    print(s.missingNumber([0,1]))
