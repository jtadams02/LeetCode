class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for x in tokens:
            if x.isnumeric() or (x[1:].isnumeric()):
                s.append(x)
            else:
                # When x is not numeric
                #print(s)
               # print(x)
                second = int(s[-1])
                s.pop()
                first = int(s[-1])
                s.pop()
                if x == "+":
                    # Addition
                    s.append(first+second)
                elif x == '-':
                    # Subtraction
                    s.append(first-second)
                elif x == '*':
                    # Multiply
                    s.append(first*second)
                elif x == '/':
                    # Floor div
                    if abs(first) < abs(second):
                        s.append(0)
                    else:
                        # This is really weird to me
                        # IDK why the math works better like this 
                        s.append(int(first/second))
                # print(s)
        if s:
            return int(s[-1])
        else:
            return 0