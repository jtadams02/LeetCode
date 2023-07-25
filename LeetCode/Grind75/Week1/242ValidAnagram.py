class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Super easy. Count the occurences of each then return

        w1 = {}
        w2 = {}
        length = max(len(s),len(t))
        for i in range(length):

            if i < len(s):
                if s[i] in w1:
                    w1[s[i]] += 1
                else:
                    w1[s[i]] = 1
            if i < len(t):
                if t[i] in w2:
                    w2[t[i]] += 1
                else:
                    w2[t[i]] = 1
        
        if w1 == w2:
            return True
        else:
            return False
        