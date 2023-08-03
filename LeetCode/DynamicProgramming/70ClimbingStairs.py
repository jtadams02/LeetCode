class Solution:
    def climbStairs(self, n: int) -> int:
        # DP Solution
        dp = [0] * (n+1)
        dp[0] = 1 # DP[0] does not exist. However, if we dont want to include an if for an edge case
        # WE need to assign dp[0] to 1 so that dp[2] = 2
        # YAY
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        # This is just a fib sequence

        # I believe
        # Not much DP here
        m = {
            1: 1,
            2: 2,
            3: 3
        }

        def climber(num,m):

            if num in m:
                return m[num]
            else:
                ans = climber(num-1,m) + climber(num-2,m)
                m[num] = ans
                return ans
        
        return climber(n,m)
            