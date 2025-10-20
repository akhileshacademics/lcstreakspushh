class Solution:
    def isPalindrome(self, s: str) -> bool:
        ssss=""
        for c in s:
            if c.isalnum():
                ssss+=c.lower()
        l,r=0,len(ssss)-1

        while l<r:
            if ssss[l]!=ssss[r]:
                return False
            l+=1
            r-=1
        return True
     



           
                    

       
        