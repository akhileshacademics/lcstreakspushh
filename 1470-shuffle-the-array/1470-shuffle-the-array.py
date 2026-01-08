class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        
        
        xn=nums[:n]
        yn=nums[n:]
        ans=[]
        for i in range(n):
            ans.append(xn[i])
            ans.append(yn[i])
        return ans




        