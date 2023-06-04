class Solution:
    def maxProfit(self, prices: List[int]) -> int:

       # Welp I thought this problem was easier than it actually was

        min_price = None
        max_profit = 0

        # What makes this solution better?
        # This solution is better because it only requires one pass
        # In every iteration of the loop, it checks whether or not the current index is lower than the minimum price
        # If it is, then the minimum price is set to the current index price

        # Otherwise, it checks to see if the price of i subtracted by the price of the minimum yields a larger profit 
        # than the current max_profit
        # This only requires one loop because it'll store the lowest value and will constantly check for more 
        for i in range(0,len(prices)):
            if min_price == None or prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

       # Below solution is brute forcing 
        low = None

        profit = 0
        for i in range(0,len(prices)):
            if low == None or (prices[i] < low and i+1 != len(prices)):
                # We have a low value, so now we need to see if we can profit
                low = high = prices[i]
                
                for x in range(i,len(prices)):
                    if prices[x] < low:
                        break
                    if prices[x] > high:
                        high = prices[x]
                    
                if (high-low) > profit:
                    profit = high-low
        
        return profit