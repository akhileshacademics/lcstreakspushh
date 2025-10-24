class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        heightmax,width=0,0

        area,maxarea=0,0

        while l<r:

            heightmax= min ( height [l] , height [r] )
            width=(r - l)
            area = heightmax * width
            maxarea=max(area,maxarea)

            if height[l]<height[r]:
                l+=1
                while l<r and heightmax >= height[l]:
                    l+=1
            else:
                r-=1
                while r>l and heightmax >= height[r]:
                    r-=1
        return maxarea



        

            
            
            

            
