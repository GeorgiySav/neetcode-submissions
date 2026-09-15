# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        i = 1

        def dfs(root):
            nonlocal i, res
            if not root or i > k:
                return

            dfs(root.left)

            if i == k:
                res = root.val
            i += 1

            dfs(root.right)

        dfs(root)
        return res