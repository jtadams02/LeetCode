class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
      # We need 2 variables
      # one keeping track of the highest altitiude and 
      # one keeping track of the total
        if gain[0] == None:
            return 0
        
        total = 0
        high = None

        for x in gain:
            total += x
            print(f"The total is: {total}")

            if not high:
                print(f"Setting high to init:{total}")
                high = total
            else:
                if total > high:
                    high = total
        
        if high < 0:
            return 0
        else:
            return high
