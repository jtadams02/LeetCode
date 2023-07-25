# I am very proud of this one
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = {}
        # Graph Problem OBV
        for x in image:
            print(x)
        def dfs(y,x,image,prev_color,new_color):
            #print(f'Coord: {y},{x}')
            if tuple([y,x]) not in visited:
                visited[tuple([y,x])] = 1
                if image[y][x] == prev_color:
                    #print('Changing')
                    image[y][x] = new_color
                    #print(image)
                    # Now we need to check its adjacencies
                    # Check upwards
                    if y-1 >= 0:
                        # Check if we can go up
                        dfs(y-1,x,image,prev_color,new_color)
                    
                    if y+1 < len(image):
                        # Check if we can go down
                        dfs(y+1,x,image,prev_color,new_color)

                    if x-1 >= 0:
                        # Check if we can go left
                        dfs(y,x-1,image,prev_color,new_color)
                    
                    if x+1 < len(image[0]):
                        #Check if we can go right
                        dfs(y,x+1,image,prev_color,new_color)
                else:
                    return
            return

        # DFS or BFS? Post-Order or Pre-Order?
        # What do they mean
        # We start at image[1][1]
        dfs(sr,sc,image,image[sr][sc],color)
        print('\nNew Graph Below\n')
        for x in image:
            print(x)
        return image

        """
        [1,2,1],
        [1,2,0],
        [1,0,1], sr = 1, sc = 1, color = 2    
        """
