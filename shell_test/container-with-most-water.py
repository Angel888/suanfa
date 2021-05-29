class Solution:
    def maxArea(self, height) :
        l=len(height)
        i,j=0,l-1
        max_aera=0
        while i<j :
            print(l,i,j)
            if height[i]<=height[j] :
                tmp_aera=height[i]*(j-i)
                i+=1
            elif height[i]>height[j] :
                tmp_aera=height[j]*(j-i)
                j-=1
            if tmp_aera>max_aera:
                max_aera=tmp_aera
        return max_aera
if __name__ == '__main__':
    s=Solution()
    # print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([4,3,2,1,4]))

