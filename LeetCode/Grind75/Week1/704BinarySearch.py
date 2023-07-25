class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Lets try this again
        # Binary search is simple, constantly cut the array in half
        def BSearch(nums,target,start,end):
            if start >= end:
                if start == end:
                    if nums[start] != target:
                        return -1
                    else:
                        return start
            
            mid = (start + end -1)//2
            if target > nums[mid]:
                # Go right
                return BSearch(nums,target,mid+1,end)
            elif target < nums[mid]:
                return BSearch(nums,target,start,mid-1)
            else:
                return mid
        return BSearch(nums,target,0,len(nums))

        left = 0
        right = len(nums) -1

        while left <= right:

            if left == right:
                if nums[left] != target:
                    return -1
                else:
                    return left
            
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                # Assuming that they equal each other
                return mid 

        return -1

            