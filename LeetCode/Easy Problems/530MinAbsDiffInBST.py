# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Solved all on my own
                

        # The Examples are using a level order traversal?
        # Kinda weird imo but whatevs

        # So for this problem, its asking us to find the minimum difference between 2 things?
        # Literally we could just traverse the tree, put each value in a queue? Placing values
        # less than at the front?

        # Lets try it
        # First We need to make a traversal of the tree
        # I really don't think that it matters that much

        q = deque()
        l = []

        # This function will do a preorder traversal of the tree and place it in our list
        def traverseHelper(node):
            if node is None:
                return
            else:
                l.append(node.val)

                if node.left:
                    traverseHelper(node.left)
                
                if node.right:
                    traverseHelper(node.right)
            
        
        traverseHelper(root)
        # Sort the list
        l.sort()

        diff = None
        for i in range(len(l)-1):
            if diff is None:
                diff = l[i+1] - l[i]
            else:
                if l[i+1] - l[i] < diff:
                    diff = l[i+1] - l[i]            

        if diff is None: return 0
        print(l)
        return diff