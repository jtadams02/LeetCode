class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        # Thinking Process:
        # We need to examine all possible pathes
        # Keep a list of visited indexs? maybe a dictionary of a list?
        # But what if it is a complex grid? Example below
        # 
        # 0 0 0 1 1 1 1 
        # 1 1 1 0 1 1 1
        # 1 1 0 1 1 1 1
        # 1 0 1 1 1 1 1
        
        # When you see a shortest path, think of BFS

        # Edge cases:
        # When we start with a 1
        if grid[0][0] == 1: return -1

        # When the last box is a 1
        if grid[-1][-1] == 1: return -1

        # Use a queue
        queue = collections.deque([(0,0,1)])

        # List of every path we can take
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        grid[0][0] = 1

        while queue:
            x, y, length = queue.popleft()

            if (x,y) == (len(grid)-1, len(grid[0])-1):
                return length
            
            for x_inc,y_inc in directions: 
                new_x = x + x_inc
                new_y = y + y_inc

                if(0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and not grid[new_x][new_y]:
                    grid[new_x][new_y] = 1

                    queue.append((new_x,new_y,length+1))
 


        return -1
    

       
        
        # Bad Solution Below
        
        # # 2D Coordinate Plane
        # x = 0 # x is horizontal
        # y = 0 # y is vertical
        # length = 1 # Count the distance
        # d = {} # Dictionary to hold coordinates visited

        # xlength = len(grid[0]) - 1
        # ylength = len(grid) - 1

        # loop_count = 0
        # back_flag = 0
        # # There is a base case where if you start at 1 then it just returns 0 so
        # if grid[0][0] == 1: return -1

        # while y != ylength or x != xlength: # This code should keep looping until the bottom right corner has been found
            
        #     # First lets add our current position to the dictionary
        #     # We could turn it into a string, since passing [x,y] wouldnt work
        #     # We only add if we arent going backwards
        #     print("Currently at x:",x,"and y:",y)
        #     if back_flag == 0:
        #         s = str(x)
        #         s += str(y)
        #         d[s] = 1
        #         loop_count += 1
            
        #     # Now that we can store it in a dictionary, lets try to move

        #     # Go diagonal first
        #     if (y+1) <= ylength and (x+1) <= xlength:
        #         st = (str(x+1)+str(y+1))
        #         if grid[y+1][x+1] == 0 and d.get(st) == None:
        #             print("going diagonally")
        #             x = x + 1
        #             y = y + 1
        #             length+=1
        #             back_flag = 0
        #             continue
                    
        #     # Moving to the right, first we need to check if its even possible 
        #     if (x+1) <= xlength:
        #         # Now that we know it is possible, lets see if we can go right, and if we've been there before
        #         st = (str(x+1)+str(y))
        #         if grid[y][x+1] == 0 and d.get(st) == None:
        #             print("going right")
        #             x = x + 1
        #             length+=1
        #             back_flag = 0
        #             continue
            
        #     # If that does not work, lets try to go down!
        #     if (y+1) <= ylength:
        #         st = (str(x)+str(y+1))
        #         if grid[y+1][x] == 0 and d.get(st) == None:
        #             print("going down")
        #             y = y + 1
        #             length+=1
        #             back_flag = 0
        #             continue
            

        #     # If we haven't moved anywhere after the first time, then we return -1
        #     if y == 0 and x == 0: return -1
        #     # We need the case where moving anywhere is impossible, if that is the case then we decrease the length and go upwards
        #     # This code should run last
        #     if y <= ylength or x <= xlength:
        #         # So we haven't gotten to the end of the graph, thats okay. Lets just move back to where we came from
        #         print("Printing dictionary before going back")
        #         print(d)
        #         counter = -2
        #         last_key = list(d)[-1]
        #         d[last_key] = 2 

        #         while d[last_key] == 2:
        #             counter-=1
        #             last_key = list(d)[counter]

        #         x = int(last_key[0])
        #         y = int(last_key[1])
        #         length -= 1
        #         back_flag = 1 
        #         # d.popitem()
        #         print("Going Back, Dict below")
            
        #     print(d)
        #     print(loop_count)
        
        # print(d)