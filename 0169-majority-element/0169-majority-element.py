class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #if majority element is not guarentied
        # count=0
        # majority=0
        # for i in range(len(nums)):
        #     if count==0:
        #         count=1
        #         majority=nums[i]
        #     elif nums[i]==majority:
        #         count+=1
        #     else :
        #         count-=1
        # count1=0
        # for i in range(len(nums)):
        #     if nums[i]==majority:
        #         count1+=1
        # if count1>len(nums)/2:
        #     return majority

        
        # if majority is guaranteed
        count = 0
        majority = 0
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            elif num == majority:
                count += 1
            else:
                count -= 1

        return majority   # if majority is guaranteed


