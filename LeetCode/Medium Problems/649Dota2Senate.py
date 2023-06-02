class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        # So after doing some research I understood how to look at this problem better
        # The best way to do this prompt would be to create a queue of each type O(n)
        # The queues contains the indexes of each character in the original senate string
        # We then compare the top of the queues. Comparing the values of the top of queues allow us
        # To tell which value will we keep.
        # For Example: 
        # R = 0 2 3 4 7
        # D = 1 5 6 
        # When we compare the two queues, whichever value is lower we will requeue in that queue with an
        # offset of size n
        # So 0 would be put back into the R queue with a value of 8 (0+8)
        # Then we can continue until one of the queues is empty. Which queue is non empty will be the correct 
        # Answer
        # All written by me, with intuition help from neetcode

        # First we need to change the string to a list
        s = list(senate)
        size = len(s)

        # After that we need to declare our queue
        D, R = deque(), deque()

        # First we need to loop through the original list and queue the indexes
        for i,c in enumerate(s):
            # i = index (reminder lol)
            if c == 'R':
                # Place in R queue
                R.append(i)
            else:
                # Place in D queue
                D.append(i)
        
        # Now we have our queues
        while R and D:
            # Lets grab our indices
            r = R.popleft()
            d = D.popleft()

            # So the problem says that each senator will use their vote to nullify the next opposite senator
            # if they can. So we need to see whos index will come first and that will tell us if they will be nullified   
            if r < d:
                R.append(r+size)
            else:
                D.append(d+size)

        # Once one of the queues are exhausted, we should be able to return the queue that wins
        if R: 
            return "Radiant" 
        else: 
            return "Dire" 
        

        # Poor intuition below
            # for x in range(len(senate)):
        #     if senate[x] == radiant:
        #         c[radiant] += 1
        #         if d[radiant] < c[radiant]:
        #             d[dire] += 1
        #     else:
        #         # There are only 2 possible choices
        #         c[dire] += 1
        #         if d[dire] < c[dire]:
        #             d[radiant] += 1
                
                    

                