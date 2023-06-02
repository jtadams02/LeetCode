class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Longest substring that has a palindrome in s
        
        # How can we approach this?
        # Well we can look at a palindrome like this. A palindrome starts
        # at an index, and for the palindrome to grow: the value of the character to the left and right
        # of an index MUST BE THE SAME
        # Example:
        # If we start with 'a', and we want to know if the resulting substring is a palindrome
        # increase 2 index variables so we get [i-1]a[i+1]. For it to be a correct palindrome, the two 
        # new VALUES MUST BE EQUAL

        # Implementation below in O(n^2) worst case?

        finalStr = ''


        # So we need to loop through the entire string and determine whether or not its a palindormic string
        for i in range(len(s)):

            # We need pointers that point to the left and right of the string
            left = right = i

            while (left >= 0 and right < len(s)) and s[left] == s[right]:
                if len(s[left:right+1]) > len(finalStr):
                    finalStr = s[left:right+1]
                left -= 1
                right += 1
            
            # Apparently even strings dont like to work so what do we do?
            left = i
            right = i+1
            # We can just offset one of the pointers. This helps us because the above code does not check if a 2 character
            # palindrome is possible. This will allow a 2 character palindrome
            while (left >= 0 and right < len(s)) and s[left] == s[right]:
                if len(s[left:right+1]) > len(finalStr):
                    finalStr = s[left:right+1]
                left -= 1
                right += 1
        
        return finalStr