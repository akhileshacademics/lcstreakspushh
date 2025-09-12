class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        freq = {}   # dictionary as hash table

    # Store frequencies of each number in nums
        for num in nums:
            freq[num] = 1   # or freq[num] = freq.get(num, 0) + 1

        for i in range(len(nums)+1):
            if i not in freq:
               return i
            

            
        


            
        
     

      