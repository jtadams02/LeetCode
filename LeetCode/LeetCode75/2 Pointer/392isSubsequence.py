class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Why did they have to allow 0 size arrays SMH
        # I am just going to assume a 0 size array is a false
        
        # that was wrong, it appears if s is empty, then we return true? 
        # Not sure what we would do if t is empty
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        # Such a simple 2 ptr question

        # p1 = 0
        p2 = 0 # I never kno whow to intiisalize ptrs correctly
        correct = -1

        for p1 in range(len(t)):
            if correct == len(s)-1: 
                return True # This will kill program?
            
            if t[p1] == s[p2]:
                # We can incrememnt p2!
                p2 += 1
                correct += 1
        
        if correct == len(s)-1: 
            return True # This will kill program?
        
        return False

