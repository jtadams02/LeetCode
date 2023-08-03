class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        rows = [[1]]

        for i in range(1,numRows):
            # Each row increases by size o 1
            new_list = []
            currIndex = 1
            # For each i we need i+1 elements in this new list
            # For example, 0 has 1 element, 1 has 2 elements, etc

            # We always start with 1?
            new_list.append(1)
            # CurrIndex wil start at 1
            while currIndex < i:
                new_list.append(rows[i-1][currIndex]+rows[i-1][currIndex-1])
                currIndex+=1 
            # Always append 1 last
            new_list.append(1)
            rows.append(new_list)
        
        return rows


