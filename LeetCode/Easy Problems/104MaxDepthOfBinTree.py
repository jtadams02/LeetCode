# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Another recursive problem
        # I SOLVED THIS FIRST TRY BABY! NO TESTING, JUST SUBMITTED IT RIGHT AWAY! I AM A GENIUS
        
        # Edge Case
        if root == None:
            return 0
        
        # Lets make a recursive function
        # I am adding a count parameter but I am not sure if we will need it
        def depthCheck(node):
            # So basically if the node is valid, we increment our count
            c = 0 # ?

            if node:
                c += 1
            
            # Now we need to recurse to the left and right
            # We're only looking for the maximum depth, we're not going to add together the depths
            # of both the left and right side
            # We want to see which side has the largest number of nodes
            # So we create a leftcount and a rightcount and set them equal to 0
            lc = rc = 0

            # If there is a valid left node, we recurse and repeat on the left side
            if node.left:
                lc = depthCheck(node.left)
            # Same with the right side
            if node.right:
                rc = depthCheck(node.right)
            # Now we just find which counter is greater and then add it too our nodeCount (which is 1)
            if lc > rc:
                c += lc
            else:
                c += rc
            # Return the counter
            return c
        
        return depthCheck(root)
            
