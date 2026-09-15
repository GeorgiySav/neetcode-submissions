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
        node_map = defaultdict(lambda: Node(0)) # node to node
        node_map[None] = None

        cur = head
        while cur:
            node_map[cur].val = cur.val
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next
        
        return node_map[head]