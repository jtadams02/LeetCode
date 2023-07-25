class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First thing we gotta do is remove all the weird stuff from the string
        newStr = ''

        for x in s:
            if x.isalnum():
                newStr+=(x.lower())
        
        # Now we just need 2 pointers
        l = 0
        r = len(newStr)-1

        while l < r:
            if newStr[l] != newStr[r]:
                return False
            
            l += 1
            r -= 1
        
        return True