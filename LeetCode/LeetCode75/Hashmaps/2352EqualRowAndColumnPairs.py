class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # All by myself?
        
        # This is a graph problem it appears
        # The question is asking whether or not there is a row/ column that is the same
        # Could we just loop and hash them?

        # Make a dictionary to hold all 

        # I think we can loop through the rows then loop through columns
        # Use 2 dictionaries. 

        r = {} # First dictionary, will hold all possible row combinations!

        # Lets start by looping through the rows
        for x in grid:
            # This loop will grab every row in order
            # Lists are not hashable, but we don't need this list to be mutable, so convert to tuple so we can hash

            nx = tuple(x)
           # print(nx)
            if nx in r:
                r[nx] += 1
            else:
                # If it isn't, add it
                r[nx] = 1
        
        # Now we need to loop through the columns
        # But how would we do that?
        # The List is ordered m x n where m is the row, and n is the column
        # Ex: For the first example List[2][1] would be 7 (Row:2,Column:1) 
        count = 0
        for i in range(len(grid[0])):

            # We're going to need a nested loop to build the list
            li = [grid[0][i]]
            # So, lets create a loop here
            for j in range(1,len(grid)):
                li.append(grid[j][i])
            # That should build the list
            #print(li)
            nx = tuple(li)
            if nx in r:
                count += r[nx]
        return count
                