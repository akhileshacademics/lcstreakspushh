class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posindex,negindex,ans=0,1,[0]*len(nums)

        for i in nums:
            if i>0:
                ans[posindex]=i
                posindex+=2
            else:
                ans[negindex]=i
                negindex+=2
        return ans
