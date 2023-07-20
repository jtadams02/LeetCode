# Finished a Medium on my own first try!
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = ['a','e','i','o','u'] # Vowel array

        # When we're dealing with sub arrays, usually a sliding window is the way to go 

        # So I think we need to do a few things here
        # First we need a win_str, and a vowel count
        win_str = deque()
        v_c = 0

        for i in range(k):
            win_str.append(s[i])
            if s[i] in v:
                v_c += 1
        
        v_max = v_c # At this point the max has to equal the initial

        # Now we can do our sliding window

        # After implementing a deque I realize how much more effort I made this.
        # There is no need for a queue or anything lol
        # Wasting memory and time with dequeu operations. We only need the v_c
        for i in range(len(s)-k):
            # String Splicing is not efficient however its what must be done
            if win_str[0] in v:
                v_c -= 1
            # Now we need to splic string
            # win_str = win_str[1:] # O(N^2) but whatever. I suppose I could use a deque
            # Beats 7.49% of all users so I am going to try a deque
            win_str.popleft() 
            # And now the dequeu only beats 23.46% What am I doing wrong?

            # Now we just repeat the same code from above?
            win_str.append(s[i+k])
            if s[i+k] in v:
                v_c += 1
            
            v_max = max(v_max,v_c)
        
        return v_max