class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding window problem, easy

        # All we need to do is define the window, then consistently move it forward
        temp_sum = 0
        avg = -1
        
        # First we need to compue the first k elements

        for i in range(k):
            temp_sum += nums[i]
        
        avg = temp_sum / k

        # Now we have the first part of our window set up. 

        for i in range(len(nums)-k):
            # Why does the below code work?
            # It works because the loop is running from 0 to len(nums) - k
            # And with every loop it is subtracting the element that gets pushed outside the window
            # when we add in a new element. It does this with -nums[i] and then adds nums[i+k] which is the right
            # edge of the window
            temp_sum = temp_sum - nums[i] + nums[i+k]
            avg = max(avg,temp_sum/k)
        return avg
