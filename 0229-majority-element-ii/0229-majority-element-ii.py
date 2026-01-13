class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen={} 
        result=[]
        if n==0 or n==1:
            return nums

        for i in nums:
            if i in seen :
                seen[i]+=1
            else:
                seen[i]=1
            
        for i in seen.keys():
            if seen[i] > n//3 :
                nums.append(i)
        return nums[n:]
