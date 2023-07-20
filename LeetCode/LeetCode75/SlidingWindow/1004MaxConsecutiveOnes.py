class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # So this is obviously a sliding window problem becasue it gives us a SET interval
        # of where to calculate numbers within 

        # The trippy thing, si that we need to figure out if we can flip some bits 

        # This one is different in the way that we will need 2 ptrs to keep track of things
        left = right = 0

        # these ptrs will allow us to determine whether or not to move the window forward
        # The left ptr will remain the same unless we have exhausted our flips 
        # Then the left ptr should increase

        # So our loop should stop when the right ptr reaches the end because it means we've exhausted 
        # All possibilities

        while right < len(nums):
            # If its a 0, lets flip it
            if nums[right] == 0:
                k-=1
            
            # If k is less than 0 though, we need to move the left ptr
            if k < 0:
                if nums[left] == 0:
                    k += 1
                
                left += 1
            
            right += 1

        return right - left

                

            

