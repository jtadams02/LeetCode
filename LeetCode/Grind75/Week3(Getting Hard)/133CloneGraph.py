"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        l = []
        def copyFunc(node,visited):
            if not node:
                return None
            
            # print(node.val)
            
            if node.val in visited:
                return visited[node.val]
            
            newNode = Node()
            newNode.val = node.val
            # This would be a lot harder in like C++ with pointers
            visited[node.val] = newNode
            # This above visited saved me. Probably would cause a bug in a real implementation
            # but VERY NICE!
            newNode.neighbors = []
            for n in node.neighbors:
                if n.val in visited:
                    newNode.neighbors.append(visited[n.val])
                else:
                    newNode.neighbors.append(copyFunc(n,visited))

            return newNode
        
        return copyFunc(node,visited)
                    


