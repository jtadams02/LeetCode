class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # 3 pointer solution?

        first, second = inf, inf

        # What this does it it uses 3 variables to keep track of values
        # It loops through the values of the array, and with each iteration, it assumes that the iterator
        # is the lowest value, or less than the second. 

        # if it is actually less than the second ptr, we can return true. 
        # This will only occur if the first ptr has a value, and the second ptr also has a value
        # The if-structure dictates that the first ptr will be assigned a value first, then if the iterator
        # is not less than first, the second ptr will receieve a value.
        # Finally, if the second ptr is less than the iterator, we can return true
        for third in nums:

            if second < third: return True
            if third <= first:
                first = third
            else:
                second = third
        
        return False