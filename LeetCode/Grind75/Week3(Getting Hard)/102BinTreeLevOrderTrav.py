# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Apparently memory is bad but whatev   
        if not root:
            return []
        
        out_list = []
        m = {}
        m[1] = [root.val]
        def levOrder(node,h):
            if not node:
                return
                
            if node.left:
                if h not in m:
                    m[h] = [node.left.val]
                else:
                    m[h].append(node.left.val)
            
            if node.right:
                if h not in m:
                    m[h] = [node.right.val]
                else:
                    m[h].append(node.right.val)
            
            levOrder(node.left,h+1)
            levOrder(node.right,h+1)
            return
        levOrder(root,2)
        for x in m:
            out_list.append(m[x])
        
        return out_list
        
                
            

            
