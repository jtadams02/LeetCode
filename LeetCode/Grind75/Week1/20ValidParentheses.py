class Solution:
    def isValid(self, s: str) -> bool:
        
        # this is a very simple stack question 
        stack = []
        if len(s) == 1:
            return False
        
        for x in s:
            if x == '[' or x == '{' or x == '(':
                stack.append(x)
            else:
                if stack:
                    if x == ']':
                        if stack[-1] != '[':
                            return False
                        else:
                            stack.pop()
                    elif x == '}':
                        if stack[-1] != '{':
                            return False
                        else:
                            stack.pop()
                    elif x == ')':
                        if stack[-1] != '(':
                            return False
                        else:
                            stack.pop()
                else:
                    return False
            
        return not stack
