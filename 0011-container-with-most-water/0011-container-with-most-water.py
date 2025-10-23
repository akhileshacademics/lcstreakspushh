class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        cur_area,width,maxarea=0,0,0

        while l<r:
            width = (r - l)
            newheight=min(height[r],height[l])
            cur_area = width * newheight
            maxarea=max(cur_area,maxarea)
            if height[l]<height[r]:
                l+=1
                while l<r and newheight>=height[l]:
                    l+=1
            else :
                r-=1
                while l<r and newheight>=height[r]:
                    r-=1
        return maxarea
            

            
