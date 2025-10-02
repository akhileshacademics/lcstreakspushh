class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even,odd,ans=0,1,[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                ans[even]=nums[i]
                even+=2
            else:
                ans[odd]=nums[i]
                odd+=2
        return ans