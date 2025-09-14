class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq={}
        for i in nums:
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1
        for i in freq:
            if freq[i]==1:
                return i
                break
                
        '''
        res=0
        for num in nums:
            res=res^num
        return res'''
                
                
                