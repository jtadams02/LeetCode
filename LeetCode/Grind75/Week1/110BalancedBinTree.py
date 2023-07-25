# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # I didnt even think to return 2 values

        def depthCheck(node):

            if not node:
                return [True,0]
            
            left = depthCheck(node.left)
            right = depthCheck(node.right)

            bal = left[0] and right[0] and (abs(left[1]-right[1]) <= 1)

            return [bal,max(left[1],right[1]) + 1]
        
        return depthCheck(root)[0]