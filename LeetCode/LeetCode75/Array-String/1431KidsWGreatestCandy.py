class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = -1
        boolArr = []
        greatests = []

        # I completely approached this problem the wrong way, I did not understand what it was asking
        # The question was just asking which of the kids will have the max candy after getting the extra candy
        # So we'd have to find the max base candy, then try adding the extras to each kid and seeing if
        # that goes over the base max candies

        # Find the max candy value 
        maxCandies = max(candies)

        # Now we iterate through the array
        for x in candies:
            if x + extraCandies >= maxCandies:
                boolArr.append(True)
            else:
                boolArr.append(False)
        
        return boolArr