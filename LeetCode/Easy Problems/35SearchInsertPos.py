class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Just a bin search with some modification

        start = 0
        end = len(nums) - 1
        mid = 0
        while start <= end:

            mid = (end-start) // 2 + start
            #print(f'Start:{start} End:{end} and Mid:{mid}')
            if target == nums[mid]:
                return mid
            elif target > nums[mid]: # Then we go right
                start = mid +1
            elif target < nums[mid]: # We go left
                end = mid - 1
        if target < nums[mid]:
            if mid == 0: # 0th index
                return 0
            else:
                return mid
        else:
            return mid+1
            