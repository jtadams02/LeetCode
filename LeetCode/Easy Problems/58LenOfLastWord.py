class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ptr = len(s)-1
        size = char_found = 0

        while ptr >= 0:
            if char_found and s[ptr].isspace():
                break
            elif char_found:
                size += 1
            else:
                if not s[ptr].isspace():
                    char_found = 1
                    size += 1
            ptr -= 1
        
        return size


