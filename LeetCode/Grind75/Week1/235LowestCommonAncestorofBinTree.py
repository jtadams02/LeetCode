# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def ancestorDetect(node,p,q):
            if node == p or node == q or not node:
                return node
            
            l = ancestorDetect(node.left,p,q)
            r = ancestorDetect(node.right,p,q)

            if l and r:
                return node
            elif l:
                return l
            elif r:
                return r
            
        
        return ancestorDetect(root,p,q)
        