class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # the dp array will go to len(cost) + 1
        # because the staircase goes to 1 over len(cost)

        dp = [0] * (len(cost) + 1)

        # I believe we can assign the second to last value
        dp[-2] = cost[-1]

        # The idea is to go backwards with the dp solution
        # At every index, find the minimum cost to get to the end
        # This is easier because if we go backwards we will have every possible cost
        # for i+1 to get to the end, so finding the cost of i to the end is easy

        # Lets implement
        
        for i in range(len(cost)-2,-1,-1):
            # Decreasing for loop

            # So at each i, we're calculating the minimum cost to get to the end
            # So, the value of dp[i] is going to be equal to the cost to use the current staircase
            # PLUS the cost of the smallest path

            # This smallest path is determined by selecting the minimum costs of 1 step/2 step
            # for example, on the second to last stair we have 2 options:
            # We can jump 2 and get to the end, or we can jump 1 and caluclate the cost of that last staircase
            # This dp solution selects the minimum of the 2: the 0 and the cost of the extra step 
            dp[i] = cost[i] + min(dp[i+2],dp[i+1])
           # print(dp)


        return min(dp[0],dp[1])
        