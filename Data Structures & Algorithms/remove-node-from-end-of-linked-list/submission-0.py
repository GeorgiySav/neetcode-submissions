# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        back, front = head, head

        for _ in range(n):
            front = front.next

        prev = None
        while front:
            front = front.next
            prev = back
            back = back.next
        
        if prev:
            prev.next = back.next
        else:
            head = head.next
        return head