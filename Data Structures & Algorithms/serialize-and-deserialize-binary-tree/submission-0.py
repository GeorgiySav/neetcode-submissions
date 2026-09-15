# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l = []

        def dfs(node):
            if not node:
                l.append("N")
                return
            l.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(l)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = data.split(',')
        i = 0

        def dfs():
            nonlocal i
            if l[i] == "N":
                i += 1
                return None
            node = TreeNode(int(l[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()