class Solution:
    def reverseWords(self, s: str) -> str:
        q = deque()
        tmp = ''
        for i in range(len(s)):
            if not s[i].isspace():
                # If the char is not a space
                tmp += s[i]
            else:
                # If the char is a space
                # print(f"Now {tmp}")
                if tmp and tmp[0] != ' ':
                    q.append(tmp)
                tmp = ''
        if tmp and tmp[0] != ' ':
            q.append(tmp)
        finalStr = ''
        while q:
            word = q[-1]
            q.pop()
            finalStr += word
            # This ensure no 
            if q:
                finalStr += ' '
        
        return finalStr
            

