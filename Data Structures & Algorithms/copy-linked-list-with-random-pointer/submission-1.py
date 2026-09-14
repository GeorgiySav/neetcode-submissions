"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {} # int to node

        def copy(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            
            node_map[node] = Node(node.val)
            node_map[node].next = copy(node.next)
            node_map[node].random = copy(node.random)
            return node_map[node]
        
        return copy(head)