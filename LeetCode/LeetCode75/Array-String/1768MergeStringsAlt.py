# 2 Pointer Solution. Runs in O(len(word1/2)) time!
# A little extra wordy but it works!
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = ''
        countOne = countTwo = 0
        flag = 0
        while True:
            if countOne >= len(word1) and countTwo >= len(word2):
                break
            elif countOne >= len(word1):
                # We only add the second word now
                newStr += word2[countTwo]
                countTwo += 1
            elif countTwo >= len(word2):
                # We only add the first word now
                newStr += word1[countOne]
                countOne += 1
            else:
                if flag == 0:
                    # Add word1
                    newStr += word1[countOne]
                    countOne += 1
                    flag = 1
                else:
                    # Add word2
                    newStr += word2[countTwo]
                    countTwo += 1
                    flag = 0
        
        return newStr
