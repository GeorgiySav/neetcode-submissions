# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0, 0
            
            left_depth, left_diameter = dfs(node.left)
            right_depth, right_diameter = dfs(node.right)
            return max(left_depth, right_depth) + 1, max(
                left_diameter,
                right_diameter,
                left_depth + right_depth
            )
        
        depth, diameter = dfs(root)
        return diameter
