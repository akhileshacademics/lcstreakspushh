class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev=[]
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                prev.append(count)

                count=0
        prev.append(count)
        return max(prev)
            
        
        