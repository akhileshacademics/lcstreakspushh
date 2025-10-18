class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        prefix,count=0,0
        remove=0
        for num in nums:
            prefix+=num
            if prefix -k in seen:
                count+= seen[prefix-k]
            seen[prefix]=seen.get(prefix,0)+1
        return count
                    

            
                
        