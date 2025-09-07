class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       # k%=len(nums)
        nums[:] = nums[-(k%len(nums)):]+nums[:-(k%len(nums))]
        
        
        
            




        """
        Do not return anything, modify nums in-place instead.
        """
        