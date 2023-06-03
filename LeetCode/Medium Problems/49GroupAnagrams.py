class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # So I was close with my sorting the strings idea
        # Basically we make a dictionary of lists
        # The key of each list would be the sorted string, and the value would be a list containing all the strings 
        # That have all those matching characters

        # To declare an empty dictionary of lists, we need to use defaultdict(list) 
        d = defaultdict(list)

        # After this, we're going to loop through the strings and sort each string. Then we use that sorted key to append the non-sorted string to that key
        for x in strs:
           temp = ''.join(sorted(x))
           d[temp].append(x)
        
        # After that we just need to loop through the dictionary and add each group to a list
        finalList = []

        for l in d:
            finalList.append(d.get(l))

        return finalList