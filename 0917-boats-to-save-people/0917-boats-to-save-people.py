class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        l,r=0,len(people)-1
        people.sort()
        boat=0
        while l<=r:
            sum=people[l]+people[r]

            if sum>limit:
                boat+=1
                r-=1
            else:
                boat+=1
                l+=1
                r-=1

        return boat

