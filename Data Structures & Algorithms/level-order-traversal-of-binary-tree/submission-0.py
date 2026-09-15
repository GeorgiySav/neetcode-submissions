# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        size = 1
        queue = deque([root])

        while queue:
            this_level = []
            next_level = 0
            for _ in range(size):
                node = queue.popleft()
                this_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                    next_level += 1
                if node.right:
                    queue.append(node.right)
                    next_level += 1
            
            levels.append(this_level)
            size = next_level
        
        return levels
                