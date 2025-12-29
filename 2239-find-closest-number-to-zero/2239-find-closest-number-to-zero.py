class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini=float('inf')
        
        for i in nums:
            diff=abs(i-0)
            mini=min(mini,diff)

        if mini in nums:
            return mini
        return -mini
