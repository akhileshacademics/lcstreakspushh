class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        dip=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                dip=i
                break
        if dip==-1:
            nums.reverse()
            return nums
        
        for j in range (n-1,dip,-1):
            if nums[j]>nums[dip]:
                nums[j],nums[dip]=nums[dip],nums[j]
                break
        nums[dip+1:]=reversed(nums[dip+1:])
        return nums

