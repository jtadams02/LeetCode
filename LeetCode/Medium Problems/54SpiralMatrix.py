class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # The matrix is of size m x n where I am assuming m = columns and n = rows
        # To do the spiral matrix, we need to move to the end of index 0, then we go down until the bottom, once we're at the bottom 

        # I think a while loop will work
        finalList = []

        # We need a Max Elements counter that will tell us when to conclude our while loop's last case
        max_elements = len(matrix[0]) * len(matrix)
        num_elements = 0
        temp_elements = 0

        rows = 0
        left_offset = 0
        right_offset = 0
        top_offset = 0
        bottom_offset = 0
        while num_elements < max_elements:
            rows = top_offset # I think?
            if temp_elements == 0:
                # When there are no elements, we add the entire first row
                for x in range(0+left_offset,len(matrix[rows])-right_offset):
                    finalList.append(matrix[top_offset][x])
                    temp_elements += 1
                rows += 1
                # We can safely increase the top offset i believe
                top_offset += 1
                if num_elements + temp_elements >= max_elements: break # The spiral loop will only break after the first row
            print(temp_elements,'first')
            if temp_elements > 0 and rows < len(matrix)-bottom_offset: # These if statements kinda dont need to be here but whatever
                # Now we need to drop to the bottom
                while rows < len(matrix)-bottom_offset:
                    finalList.append(matrix[rows][len(matrix[rows])-left_offset-1])
                    temp_elements += 1
                    rows += 1
                print(temp_elements,'second')
                # Add another check to kill the loop
                if num_elements + temp_elements >= max_elements: break
            # The initial loop should be completed, now we need to go backwards. Update the Horizontal Offset
            right_offset += 1
            rows -= 1 # The rows decrease too much with the above loop

            # At this point, we want to run along the bottom
            if rows == len(matrix) - bottom_offset - 1: # Again, pretty redundant
                # Now we need to loop backwards through the bottom list
                for i in range(0+left_offset,len(matrix[rows])-right_offset):
                    finalList.append(matrix[rows][len(matrix[rows])-right_offset-1-i+left_offset]) # We need to subtract the one to not re-add the right most element
                    print(matrix[rows][len(matrix[rows])-right_offset-1-i+left_offset])
                    temp_elements += 1
                # Again, check if the array is complete
                if num_elements + temp_elements >= max_elements: break
                # Now the entire bottom row should be added, so increase the bottom offset
                bottom_offset += 1
                # And its time to go upwards, which I shall take care of in this same if statement
                rows -= 1 # Set the row indicator to the one above the bottom

                while rows > top_offset - 1:
                    finalList.append(matrix[rows][left_offset])
                    temp_elements+=1
                    rows -= 1
                # Again, check if we finished
                left_offset += 1
                if num_elements + temp_elements >= max_elements: break
            
                num_elements += temp_elements
                temp_elements = 0 # Reset the temp counter
            print(num_elements,'looping')
            

        # WAIT WE RECURSE, WE GO ALONG THE BOTTOM THEN RESTART HOLY MOLY 
                
        

        return finalList
            
