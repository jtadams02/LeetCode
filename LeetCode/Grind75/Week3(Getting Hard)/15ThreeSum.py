class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # So the way to solve this is to reduce this to a two sum

        nums.sort()
        # First we sort the array

        # Then we use the 2 ptr approach I discovered (on my own) in Two Sum II
        out_arr = []
        i = 0
        print(nums)
        while i < len(nums): # -2 offset for 2 ptrs
                if i > 0 and nums[i] == nums[i-1]:
                    i+=1
                    continue
                l = i + 1
                r = len(nums)-1

                while l < r:
                    # If they equal they should break
                    ts = nums[l] + nums[r] + nums[i]
                    if ts == 0:
                        # Match found!
                        out_arr.append([nums[i],nums[l],nums[r]])
                        # But what happens when we find a match? 
                        # Where do we reduc
                        # Both or what?
                        # My first thought is to inc left cuz its the smaller num and would have less of an effect?
                        # Idk mathematically there shouldnt be another possible solution so if I do inc left then
                        # the next iteration would automatically dec right with this if statement below
                        l += 1
                        # Did not account for duplicates in the same sub-while loop
                        while nums[l] == nums[l-1] and l < r:
                            l+=1
                    else:
                        if ts > 0:
                            # We need to reduce the right
                            r -= 1
                        else:
                            # We need to reduce left
                            l += 1
                i+=1
        return out_arr


        
        