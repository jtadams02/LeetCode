class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # if the lengths of the strings are not equal, return false
        if len(word1) != len(word2):
            return False
        
        # First, lets dump everything into our hashmaps
        w1 = {}
        w2 = {}

        # We actually could use counter objects
        # I just learned about them and they are really cool
        c1 = Counter(word1) # This will tall all the occurences of each character in word1
        c2 = Counter(word2) # This will tally all the occurences of each character in word2
        # If the counters are the exact same, we can just return true
        # This is very similar to the below code where I check if the keys are the same!
        if c1 == c2:
            return True
        
        # That would handle an strings that could be made the same from Op1 only. But Op2 deals with the frequecies of 
        # strings

        # The frequencies must all be the same in both strings
        # The below counters check the how many times the frequency of a character appears
        # For example 1, there are 3 frequencies of 1 occurence.
        # All this means is that 
        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])
        
        if n1 == n2 and set(word1) == set(word2):
            return True

        return False
        # Operation 1
        # Op1 can only be done if the 2 dictionaries equal one another
        # We need a swap 1 operation first
        if w1.keys() == w2.keys():
            return True
        
        return False