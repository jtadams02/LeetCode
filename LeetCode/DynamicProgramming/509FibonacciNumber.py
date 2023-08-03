class Solution:
    def fib(self, n: int) -> int:

        # Fib with memoization I am guessing

        m = {} # Memory
        m[0] = 0
        m[1] = 1

        def fibby(num,m):
            if num in m:
                # print("In memory table!")
                return m[num]
            else:
                ans = fibby(num-1,m) + fibby(num-2,m)
                m[num] = ans
                return ans
        
        return fibby(n,m)
