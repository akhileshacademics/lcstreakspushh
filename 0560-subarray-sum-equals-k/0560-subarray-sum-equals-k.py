class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        prefix,count=0,0
        remove=0
        for i in range(len(nums)):
            prefix+=nums[i]
            remove=prefix-k
            count+=seen.get(remove,0)

            seen[prefix]=seen.get(prefix,0)+1
        return count

        
                    

            
                
        