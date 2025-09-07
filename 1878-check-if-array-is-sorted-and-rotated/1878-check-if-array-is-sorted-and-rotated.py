class Solution:
    def check(self, nums: List[int]) -> bool:
        
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
        if nums[-1] > nums[0]:
            count += 1

        return count <= 1

         
'''
count = 0
n = len(nums)
for i in range(n):
    if nums[i] > nums[(i+1) % n]:
        count += 1
return count <= 1


'''

                