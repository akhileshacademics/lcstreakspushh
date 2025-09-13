class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev=0
        count=0
        for i in nums:
            if i==1:
                
                count+=1
                prev=max(count,prev)
            else:
                count=0
        return prev
            
        
        