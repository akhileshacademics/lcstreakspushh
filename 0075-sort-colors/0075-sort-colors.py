class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0,count1,count2=0,0,0
        for i in nums:
            if i ==0:
                count0+=1
            if i==1:
                count1+=1
            if i==2:
                count2+=1
        for i in range(count0):
            nums[i]=0
        for i in range(count0,count0+count1):
            nums[i]=1
        for i in range (count0+count1,len(nums)):
            nums[i]=2
        
        return nums