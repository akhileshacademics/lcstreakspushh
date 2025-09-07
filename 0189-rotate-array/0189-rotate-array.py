class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       # k%=len(nums)
        nums[:] = nums[-(k%len(nums)):]+nums[:-(k%len(nums))]
        
        
        
            




        """
        def rotate(nums, k):
            n = len(nums)
            k %= n
            nums[:] = nums[-k:] + nums[:-k]   # modify in place

        
        """
        