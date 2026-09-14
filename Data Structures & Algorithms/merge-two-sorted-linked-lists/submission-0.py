# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        buffer = ListNode()
        res = buffer
        while list1 and list2:
            if list1.val < list2.val:
                buffer.next = list1
                list1 = list1.next
            else:
                buffer.next = list2
                list2 = list2.next
            buffer = buffer.next

        while list1:
            buffer.next = list1
            list1 = list1.next
            buffer = buffer.next
        while list2:
            buffer.next = list2
            list2 = list2.next
            buffer = buffer.next
        
        return res.next