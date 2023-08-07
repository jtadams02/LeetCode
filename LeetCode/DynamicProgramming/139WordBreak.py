class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom up DP 
        n = len(s)
        dp = [False] * (n+1)

        dp[n] = True    
        # print(dp)
        for i in range(len(s)-1,-1,-1):
            print(i)
            for w in wordDict:
                # The first condition checks if the current index i added to the length
                # of the current word is less than len(s), or can it fit in the string
                # Then the second checks if string from i to i+len(w) is equal to the word
                # Just checks if we have a complete word at this index
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    print('yay')
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]
        