class Solution:
    def reverse(self, x: int) -> int:
        # I solved this problem already, but I used a hacky way to solve it, 
        # I'm now going to implement a better solution to solve this problem

        # I did comparison operations which exceeded the 32 bit limit, for this problem we're assuming that is not possible

        # Starting with a 0 makes this all wonky so lets edge case it
        if x == 0:
            return 0
        
        max32 = 2147483647
        min32 = 2147483648
        tempInt = x 

        finalInt = 0

        if tempInt < 0: 
            tempInt = tempInt * -1

        # We need to make sure that a beginning 0 is handled
        if tempInt % 10 == 0:
            tempInt /= 10
        # The above code should remove the beginning 0

        while tempInt != 0:
            # Lets grab the back of tempInt
            single = tempInt % 10
            print(tempInt,single)

            # Now that we have the back we need to check if adding it to the final int will break everything
            # The best wasy to check if it will fit would be to remove the last digit of the 32 bit

            if x < 0:
                # Negative input will run
                temp32 = min32 // 10
                print('temp is ',temp32)
                if finalInt-temp32 >= 0:
                    # This code runs when the final int is larger
                    # We now need to check to see how large the difference is
                    if finalInt - temp32 == 0 and single <= 8:
                        # We can insert
                        finalInt = finalInt * 10
                        finalInt += single
                    else: 
                        return 0

                else: 
                    # Otherwise just add it
                    finalInt = finalInt * 10 
                    finalInt += single

            else: 
                # Positive input will run
                temp32 = max32 // 10
                print('temp is',temp32)

                if finalInt - temp32 >= 0:
                    print('oops')
                    # This code will run when the finalInt is bigger than the max32 without its singles digit
                    # If this happens, we need to check to see if we can actually put a new number in
                    # We can only add 7 so we need to see if there is enough space for 7
                    if finalInt-temp32 == 0 and single <= 7:
                        # Here we can add in our single digit
                        finalInt = finalInt * 10
                        finalInt += single
                    else: 
                        # This code will run when the difference between finalInt and reduced max32
                        # is more than 7 or when the single is more than the difference
                        return 0
                else:
                    # This code runs when the finalInt does not equal the reduced max32, this means we can safely insert
                    finalInt = finalInt * 10
                    finalInt += single

            print('finalInt is',finalInt)
            tempInt = tempInt // 10
        
        if x < 0:
            return int(finalInt * -1)
        else:
            return int(finalInt)



        # Hacky Solution

        # # 0 is an edge case which causes an error with the below code so lets take care of it
        # if x == 0:
        #     return 0
            
        # # I think dealing with a string may be easier here

        # isNeg = True if x < 0 else False
        # s = str(abs(x))

        # # Now lets reverse it
        # rev = s[::-1] # Special reverser code

        # print(rev)
        # if int(rev) > 2147483647: # Out of bounds checking
        #     return 0
        

        
        # final = rev
        # if int(rev[0]) == 0:
        #     # If it starts with a 0
        #     final = rev[1:]
        
        # final = int(final)
        # if x > 0:
        #     return final
        # else: 
        #     return final * -1

