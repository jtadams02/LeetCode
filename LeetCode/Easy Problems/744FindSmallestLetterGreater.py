class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # There is a much more efficient solution where we break right after finding that first new letter
        # This is because the list of letters is sorted in non-decreasing order, so the next letter after the target will always be the correct answer if it is 
        # valid
        letter = target
        for x in letters:
            if letter == target:
                # This will take care of just getting the final letter tracker to something other than the target
                if x > letter:
                    letter = x
            else:
                # Otherwise we need our comparisons
                if x > target and x < letter:
                    letter = x

        if letter == target:
            return letters[0]
        else:
            return letter