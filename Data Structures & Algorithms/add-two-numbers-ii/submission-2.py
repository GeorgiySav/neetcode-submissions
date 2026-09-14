# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_to_num(l: Optional[ListNode]):
            num = 0
            while l:
                num = (num * 10) + l.val
                l = l.next
            return num
        
        def num_to_linked(i):
            buffer = ListNode(0)
            cur = buffer
            for c in str(i):
                cur.next = ListNode(0)
                cur = cur.next
                cur.val = int(c)
        
            return buffer.next

        return num_to_linked(linked_to_num(l1) + linked_to_num(l2))