class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        cur_area,width,maxarea=0,0,0

        while l<r:
            width = (r - l)
            cur_area = width * min(height[r],height[l])
            maxarea=max(cur_area,maxarea)
            if height[l]<height[r]:
                l+=1
            else :
                r-=1
        return maxarea
            

            
