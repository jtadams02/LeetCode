class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Seems like a hashmap problem but thats okay

        # Sol3 

        

        # Sol2
        r = {}
        for x in ransomNote:
            if x in r:
                r[x] += 1
            else:
                r[x] = 1
        m2 = {}
        for x in magazine:
            if x in r:
                if x in m2:
                    if m2[x] < r[x]:
                        m2[x] += 1
                else:
                    m2[x] = 1
        return r == m2
        # Hashmap for the magazine
        m = {}

        for x in magazine:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        
        # Now we need to loop through ransom note

        for x in ransomNote:

            if x in m:
                if m[x] > 0:
                    m[x] -= 1
                else:
                    return False
            else:
                return False
        
        return True
