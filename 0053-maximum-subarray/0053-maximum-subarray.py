class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxy=float("-inf")
        sum=0
        for i in nums:
            sum+=i
            if maxy==float("-inf"):
                maxy=i
            else:
                maxy=max(sum,maxy)
            if sum<0:
                sum=0
        return maxy