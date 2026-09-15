# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def balanced(node):
            if not node:
                return True, 0
            
            lb, ld = balanced(node.left)
            if not lb:
                return False, 0
            
            rb, rd = balanced(node.right)
            if not rb:
                return False, 0
            
            return abs(rd - ld) <= 1, max(rd, ld) + 1
        
        b, d = balanced(root)
        return b