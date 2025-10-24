class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        area,width=0,0
        maxsum=0

        while l<r:
            width=(r-l)

            new=min(height[l],height[r])
            cur_sum=new*width
            maxsum=max(cur_sum,maxsum)

            if height[l]<height[r]:
                l+=1
                while l<r and new>=height[l]:
                    l+=1
            else:
                r-=1
                while r>l and new>=height[r]:
                    r-=1
        return maxsum

            
            
            

            
