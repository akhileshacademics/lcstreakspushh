class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range (len(nums)):

            nums[i]=abs(nums[i]*nums[i])
        l,r=0,len(nums)-1
        
        nums.sort()

        return nums

        