
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # ALL ON MY OWN BABY
        # Sort and then 2 ptrs
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums)-1

        nums.sort()
        op_count = 0

        # First thing we need to do is wait until the right is pointing to a value that is less than k
        while(nums[right] > k):
                right -= 1
                if right <= 0:
                    return 0

        while(left < right):
            if nums[left] + nums[right] >= k:

                if nums[left] + nums[right] == k:
                    left += 1
                    right -= 1
                    op_count += 1
                else:
                    right -= 1
            else:
                # If its less than k we move left forward
                left += 1
        return op_count
        