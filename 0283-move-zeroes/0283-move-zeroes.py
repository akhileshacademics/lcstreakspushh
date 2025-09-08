class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #sliding window
        j=0
        for i in range(len(nums)):

            if nums[i]!=0 and nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                
            if nums[j]!=0:
                j+=1
        return nums
            