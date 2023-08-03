class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = {}
        for x in s:
            if x in h:
                h[x] += 1
            else:
                h[x] = 1
        
        pal_len = 0
        odd_len = 0
        odd_flag = 0
        for x in h:

            if h[x] %2 == 0:
                pal_len += h[x]
            else:
                # If odd
                # We can only have 1 odd
                if not odd_flag:
                    odd_flag = 1
                    pal_len += h[x]
                else:
                    pal_len += h[x] - 1
        return pal_len


        