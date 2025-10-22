class Solution:
    def maxArea(self, height: List[int]) -> int:

        area,width,left,right,maxarea=0,0,0,len(height)-1,0

        while left < right:

            width = (right - left)
            area = width * min(height[left],height[right])
            maxarea=max(area,maxarea)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea

            

            
