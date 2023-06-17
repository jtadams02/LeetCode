    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Inverting a binary tree is relatively simple
        # All we need to do is swap each nodes children

        # We can use recursion for this
        def invert(node: Optional[TreeNode]):
            # If the head is none, we just return ?
            if node == None:
                return

            # We need temp variables to hold the left and right children
            left = node.left
            right = node.right

            # And legit all we do is just swap them
            node.left = right
            node.right = left

            if node.left != None:
                invert(node.left)
            
            if node.right != None:
                invert(node.right)
            
        invert(root)

        return root
            