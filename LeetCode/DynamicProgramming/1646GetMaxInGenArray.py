class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # this feels like a mix of fib and something wierd
        # dp feels like the way to go
        if n == 0:
            return 0 # Stupid
            
        nums = [0] * (n+2)
        nums[1] = 1

        for i in range(1,n+1):
            if 2<= 2*i and 2*i <= n:
                nums[2*i] = nums[i]
            else:
                break

            if 2 <= 2 * i + 1 and 2 * i + 1 <= n:   
                nums[2*i+1] = nums[i] + nums[i+1]

        return max(nums)
        
        


