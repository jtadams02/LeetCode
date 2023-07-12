class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Going to need to use lots of str splices with this one
        # Definitely costly operations but whatever

        # Below code finds the largest and smallest string as we need them
        smallest_word = str2
        largest_word = str1

        if len(str1) < len(str2):
            smallest_word = str1
            largest_word = str2

        for i in range(len(smallest_word),0,-1):
            # Just a check to make sure that each str is evenly divisible
            if len(str1) % i or len(str2) % i:
                continue
            # Lets create our base splice
            base = smallest_word[:i]
            # And figure out how many times it goes into the larger word
            times = len(largest_word) // len(base)
            times2 = len(smallest_word) // len(base)
            # Now we just need to check if it can go into the largest string
            # If it does, return
            if base * times == largest_word and base * times2 == smallest_word:
                return base
        
        return ''
