class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        
        rangestart=min(nums)
        rangeend=max(nums)
        keep=[]
        numset=set(nums)
        j=0
        for i in range(rangestart,rangeend):

            if i not in numset:
                keep.append(i)
            j+=1

        return keep

            