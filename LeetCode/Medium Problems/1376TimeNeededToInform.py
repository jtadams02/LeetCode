class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # I really struggled with this problem
        # I needed some help from Youtube to solve it
        # I still dont quite understand how this works 
        
        # BFS 
        # Layer by Layer
        # Done with a queue data structure

        # Build an adjaceny list !
        adj = collections.defaultdict(list)
        # Map the Manager to list of employees
        for i in range(n):
            adj[manager[i]].append(i)
        
        # BFS 
        q = deque([(headID,0)]) # Contains pairs where we have an ID and a number

        res = 0

        while q:
            i, time = q.popleft()
            res = max(res,time)

            for emp in adj[i]:
                q.append((emp, time + informTime[i]))


        return res
