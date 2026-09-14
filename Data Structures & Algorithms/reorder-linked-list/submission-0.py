# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            right = cur.next
            cur.next = prev
            prev = cur
            cur = right
        
        l1, l2 = head, prev
        while l1 and l2:
            nl1 = l1.next
            nl2 = l2.next
            l1.next = l2
            l2.next = nl1
            l1 = nl1
            l2 = nl2