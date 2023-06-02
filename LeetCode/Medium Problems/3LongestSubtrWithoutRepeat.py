class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # This solution was apparently much slower
        
        # Edge case when size is 1:
        if len(s) == 1:
            return 1
        # This one doesnt seem that hard
        # Just create a dict with each substring and if the value already exists then break
       # largetString = ''
        count = 0
        

        for x in range(0,len(s)):
            # Initalize dictionary
            d = {}
            substr = s[x]
            #print("Begining value:",substr)
            d[s[x]] = 1
            tempCount = 1
            # For each char we build a substring
            for i in range(x+1,len(s)):
                c = s[i] # char holder
                #print("Next char",c)
                if c in d: # if the char is in the dictionary, then it must be a repeat value so kill the loop
                    #print("Breaking!")
                    break
                else: 
                    substr += c
                    tempCount += 1
                    d[c] = 1
                    #print("Current Substring:",substr)
            
            # When we reach the end of the for loop we must update the count
            if tempCount > count: count = tempCount; #print("Updating Count")
        

            # Now we return to the while loop

        return count
