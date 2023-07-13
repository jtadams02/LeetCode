class Solution:
    def reverseVowels(self, s: str) -> str:
        # We can use a queue for this
        # Probably will take a queue
        q = deque()

        vowels = ['a','e','i','o','u'] # And sometimes letter y!
        newStr = ''

        for i in range(0,len(s)):
            if s[i].lower() in vowels:
                q.append(s[i])
        
        # Now we need to reiterate
        for i in range(0,len(s)):
            if s[i].lower() in vowels:
                replace_char = q[-1]
                q.pop()
                newStr += (replace_char)
            else:
                newStr += (s[i])
        
        return newStr