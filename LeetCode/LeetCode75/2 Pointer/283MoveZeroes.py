class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,1,0,3,12]
        
        # How can we approach this?
        
        # If we're doing in place, we're going to need a way to iterate through the array.
        # Find a 0, then find the next place we can put it 
        # This is not the cleanest 2 ptr solution, but it essentially does the 
        # same thing
        for i in range(len(nums)):
            if nums[i] == 0:
                # Now we need to find a place to swap it
                for j in range(i+1,len(nums)):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        
