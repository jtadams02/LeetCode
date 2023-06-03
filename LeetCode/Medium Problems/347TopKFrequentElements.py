class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Notes on Intuition:
        # 

        # Edge case when the array is of size 1
        if len(nums) == 1:
            return [1]


        # I'm going to start with a dictionary
        d = {}
        
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        
        # K is guaranteed to be in the range of unique values so that is not an issue

        # print(d)
        finalList = []
        # Now we need to loop through the dictionary to find the most frequent value
        # We will do this K times, and add them to the final list
        # There has to be a more efficient way to do this but this is just what I am going for right now

        c = 0
        # There has to be a way to sort the dictionary but I am newer to Python and am not aware of it so we're going to do a slightly longer solution  
        while c < k:
            highestFreq = 0
            val = 0

            for j in d:
                if d[j] > highestFreq:
                    highestFreq = d[j]
                    val = j
                    # print(f'j {j}')
            
            # After that highestFreq should be equal to the int that appears the most times
            # Now we can remove that key from the dictionary using pop()
            finalList.append(val)
            d.pop(val)
            # print(d)
            # Increment our loop condition c
            c += 1

        # That should populate the dictionary with the total counts

        return finalList
            
