class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # For this solution, we probably want to use a dictionary. Or we could use a hashmap
        d = {}
        d2 = {}

        # Edge case my dictionary loop doesnt account for differnt string lengths
        # But different string lengths just mean that they cannot be anagrams
        if len(s)!=len(t):
            return False

        # Could we use 2 dictionaries and compare the values?
        # Bad runtime but is a solution

        # For an anagram, they must have the same exact letters, so we can loop through just one
        for x in s:
            # Lets check if the character exists in the dictionary
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
        
        # Now lets repeat the process for the string t
        for x in t:
            if x in d2:
                d2[x] = d2[x] + 1
            else:
                d2[x] = 1

        # Now we're going to loop through the first dictionary
        for x in d:
            if x in d2:
                # Now we're checking if both dictionaries have the same key, if they do, we need to make sure they also have the same value
                if d[x] != d2[x]:
                    return False
            else: 
                return False
        return True