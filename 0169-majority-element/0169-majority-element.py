class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        for i in seen.keys():
            if seen[i]>n/2:
                return i 
        