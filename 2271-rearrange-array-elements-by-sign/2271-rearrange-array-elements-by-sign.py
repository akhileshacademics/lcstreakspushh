class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posindex,negindex,ans=0,1,[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]>0:
                ans[posindex]=nums[i]
                posindex+=2
            else:
                ans[negindex]=nums[i]
                negindex+=2
        return ans
