# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # To invert a binary tree all we need to do is swap the chidren

        def invertTree(node):
            if node:
                tempr = node.right
                templ = node.left
                node.left = tempr
                node.right = templ
                # Now we need to recurse downwards
                node.left = invertTree(node.left)
                node.right = invertTree(node.right)
                return node
            else:
                return None

        root = invertTree(root)
        return root