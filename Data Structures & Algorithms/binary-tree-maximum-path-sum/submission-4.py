# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, -float('inf')
            if not node.left and not node.right:
                return max(0, node.val), node.val
            
            left_l, left_m = dfs(node.left)
            right_l, right_m = dfs(node.right)
            
            l = max(left_l + node.val, right_l + node.val)
            return l, max(
                left_l + node.val + right_l,
                left_l + node.val,
                right_l + node.val,
                left_m,
                right_m,
                node.val
            )
        
        return dfs(root)[1]