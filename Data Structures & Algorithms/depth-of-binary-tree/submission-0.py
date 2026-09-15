# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, d):
            if not node:
                return 0

            if not node.left and not node.right:
                return d
            
            return max(dfs(node.left, d+1), dfs(node.right, d+1))
        
        return dfs(root, 1)