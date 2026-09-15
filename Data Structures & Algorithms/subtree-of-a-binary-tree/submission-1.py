# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        def subtree(node, sub):
            if not node and not sub:
                return True
            if node and not sub:
                return False
            if not node and sub:
                return False
            if node.val != sub.val:
                return False
            return subtree(node.left, sub.left) and subtree(node.right, sub.right)
        
        return subtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)