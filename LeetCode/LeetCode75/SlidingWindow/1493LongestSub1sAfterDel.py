# Finished this question ALL ON MY OWN!
# Not the most efficient but oh well
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # Lets build our small window
        right = left = 0
        w_size = 0
        one = 0
        zero_pos = 0
        w_max = 0
        while right < len(nums):
            # If we've already deleted an element
            if one:
                if nums[right] == 0:
                    break # Our right ptr will point to the first element outside the window
                else:
                    w_size += 1
                    w_max = max(w_size,w_max)
            else:
                if nums[right] == 0:
                    one = 1
                    zero_pos = right
                    # w_size += 1 We don't actually increment here we just ignore it 
                else:
                    w_size += 1
                    w_max = max(w_size,w_max)
            right += 1
        
        if right == len(nums):
            if one:
                # If we've deleted a vlaue, we can just return w_max
                return w_max
            else:
                return w_max - 1
        
        #print(f"Initial window is from index {left} to index {right-1} and is of length {right-left}")
       # print(nums[:right])

        # Now we need to go through the rest
        # We can go until right reaches the end
        while right < len(nums):
            if nums[right] == 0:
                # If the new element is a 0, we need to text a few things
                # First we need to determine if our left is a 0
                if nums[left] == 0:
                    # This is good, we can just increment left and continue
                    one = 0
                    left += 1
                else:
                    # Otherwise if the 0 is somewhere else, we may have issue
                    # I think we'll need to decrement window size and move left until we reach 0
                    while(nums[left] != 0):
                        left += 1
                        w_size -= 1
                    # Now left should be 0
                    one = 0
                    left += 1
                    # I don't think we should need to do anything with the window size
                    # But it would be right - left - 1 (We don't count the 0)
            else:
                # If the rightmost value is not a 0, we can increase window size and continue!
                w_size += 1
                w_max = max(w_size,w_max)
            
            # And increment right
            right += 1



        return w_max


