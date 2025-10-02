class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxy=nums[0]
        sum=0
        for i in nums:
            sum+=i
            if sum>maxy:
                maxy=sum
            if sum<0:
                sum=0
        return maxy