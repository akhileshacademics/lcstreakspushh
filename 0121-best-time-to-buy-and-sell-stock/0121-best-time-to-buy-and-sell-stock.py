class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            cost=prices[i]-min
            if  cost>maxprofit:
                maxprofit=cost
            if prices[i]<min:
                min=prices[i]

        return maxprofit

        
       