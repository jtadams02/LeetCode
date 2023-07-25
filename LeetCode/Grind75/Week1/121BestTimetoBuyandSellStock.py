class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # I feel like this is a sliding window problem 
        # Lets attempt it like that
        
        left = 0
        right = 1

        max_profit = 0
        low = prices[0]

        for x in prices:
            if x < low:
                low = x
            max_profit = max(max_profit,x-low)
        
        return max_profit


        