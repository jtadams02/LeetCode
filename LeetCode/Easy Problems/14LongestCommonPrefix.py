class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        finalSubstr = ""
        kill = 1
        spot = 0
        # This loop will grab every character in the first substring
        for x in strs[0]:
            # Loop through the rest of the strings and see if the char is at the same location in each str
            for i in range(1,len(strs)):
                # If the index of spot is too big, or it doesnt match the char, kill the loop
                if spot >= len(strs[i]) or strs[i][spot] != x: return finalSubstr
            # Otherwise, add the character to the final substring, increase the index and keep counting
            finalSubstr += x
            spot += 1




        return finalSubstr