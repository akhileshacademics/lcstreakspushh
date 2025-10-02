class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxy=nums[0]
        cursum=0
        for i in nums:
            if cursum<0:
                cursum=0

            cursum+=i

            if cursum>maxy:
                maxy=cursum
            
        return maxy