class Solution:
    def removeStars(self, s: str) -> str:

        # This ones so simple
        # The most basic stack

        # Solved this one in like 1 minute lol
        r = []
        
        for x in s:
            if x == '*':
                # Do something 
                r.pop()
            else:
                r.append(x)
        
        rs = ''.join(r)
        return rs
            