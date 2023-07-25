class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        # Now the table is initalized 

        for i in range(len(nums)):
            diff = target - nums[i]
            # We need to see if d[x] is valid
            if diff in d:
                if d[diff] != i:
                    return [i,d[diff]]

        return []