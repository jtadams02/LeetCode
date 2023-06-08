class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Really simple
        # Just for loop in range backwards, break the loop when grid[i] >= 0
        total_count = 0
        for i in range(len(grid)):
            c = 0
            for x in reversed(grid[i]):
                if x < 0:
                    c += 1
                else: 
                    break
            total_count += c
        return total_count
