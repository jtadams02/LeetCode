class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Disclaimer: In all honesty, I am not quite sure why this code worked
        # I get the logic of binary search, but my implementation was struggling in terms of accessing indices out of bounds
        # I was just kinda hacking at it and it just worked, hopefully I can understand why in a second

        # Binary Search is the process of searching through a sorted list 
        # To find a value
        # It works by looking at the value in the index that is half the length of the 
        # array, and then if the target is >, it looks from half-end, if the target is < half, then it
        # looks from 0-half-1

        # I believe a recursive solution would be the most ideal thing to use
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def binSearch(nums: List[int], target: int, start: int, end: int):
            # To select the middle element, we need to subtract the start from the end and divide it by 2.
            # Then we need to add the start value again as an offset
            # For example: if our array is [1,3,5,7,8,9], start = 0 and end = 6
            # diff = start - end or 6. And 6//2 == 3. so we'd select the 4th element which is 7.
            # From there if our target was 9, we'd need to look at 8,9 on our next call
            # so our diff would be diff = end(6)-start(3) // 2 which would yield 1. But we don't want to check the
            # index of 1 do we? No, we want to check the element that is 1 in front of our previous element. So
            # we add the starting index of 3 to this, giving us a diff of 4 and the number we look at would be 8.
            # 8 is less than 9 so we recurse on the right side. Our start is 4, and end is still 6. diff = 6-4 // 2 which is 1 again
            # so we add the previous start of 4 to get the index of 5. Checking index 5 we see that it is in fact the target and we return our diff index
            diff = (end - start)//2 + start

            if nums[diff] == target:
                return diff
            elif (end-start) == 1:
                # If the difference of the 2 numbers is 1, and there is no matching element
                # we can return -1 because we've made it to the smallest possible difference, so there's no other path 
                # we can take to recurse through
                return -1
            
            # Otherwise
            if target > nums[diff]:
                return binSearch(nums,target,diff,end)
            else:
                return binSearch(nums,target,start,diff)

            
        return binSearch(nums,target,0,len(nums))

        return 0