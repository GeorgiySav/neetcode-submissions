# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_depth = 0

        def dfs(node, d):
            nonlocal res, max_depth

            if not node:
                return
            
            if d > max_depth:
                res.append(node.val)
                max_depth = d
            
            dfs(node.right, d+1)
            dfs(node.left, d+1)
        
        dfs(root, 1)
        return res