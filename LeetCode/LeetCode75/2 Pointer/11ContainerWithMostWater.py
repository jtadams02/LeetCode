class Solution:
    def maxArea(self, height: List[int]) -> int:

        # This is an interesting problem
        # I feel the ideal solution is to start with 2 ptrs on opposite sides and slowly move inwards
        # I dont know how to handle which ptr to change though

        l = 0
        r = len(height) - 1

        max_area = -1

        l_val = height[l]
        r_val = height[r]

        while l <= r:
            l_val = height[l]
            r_val = height[r]
            temp_height = min(l_val,r_val)
            temp_width = r-l

            temp_area = temp_height * temp_width

            max_area = max(temp_area,max_area)
            
            if min(l_val,r_val) == r_val:
                r -= 1
            else:
                l += 1
        return max_area

        # this works but is very inefficient



            
