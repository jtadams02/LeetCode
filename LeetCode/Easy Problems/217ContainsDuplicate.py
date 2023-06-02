class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Very simple problem, we can just use a dict
        d = {}
        for x in nums:
            if d.get(x) != None:
                return True
            else:
                d[x] = 1
        return False