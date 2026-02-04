class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        
        prefix =1
        suffix=1
        ans= float('-inf')


        if len(nums)==1 and nums[0]<0:
            return nums[0]

        for i in range(len(nums)):

            if (prefix==0):
                prefix=1
            if (suffix==0):
                suffix=1

            prefix*=nums[i]
            suffix*=nums[len(nums)-i-1]

            ans=max(ans,max(prefix,suffix))

        return ans