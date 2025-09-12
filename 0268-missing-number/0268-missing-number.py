class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        freq = {}   # dictionary as hash table

    # Store frequencies of each number in nums
        for num in nums:
            freq[num] = 1   # or freq[num] = freq.get(num, 0) + 1

        #list(range(len(nums)+1))
        return(sum(list(range(len(nums)+1)))-sum(nums))

            
        


            
        
     

      