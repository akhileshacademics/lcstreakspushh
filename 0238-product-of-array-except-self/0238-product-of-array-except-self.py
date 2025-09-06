from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, answer = [1]*n, [1]*n, [1]*n
        
        # Compute prefix products
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # Compute suffix products
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # Multiply prefix and suffix
        for i in range(n):
            answer[i] = left[i] * right[i]
        
        return answer



     
