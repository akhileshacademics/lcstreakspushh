class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxy=nums[0]
        sum=0
        for i in nums:
            sum+=i
            maxy=max(sum,maxy)
            if sum<0:
                sum=0
        return maxy