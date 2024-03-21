# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        start = head
        while start.next:
            length += 1
            start = start.next
        if length == 1:
            return None
        else:
            start = head
            if length - n ==0:
                return head.next
            for i in range(length-n-1):
                start = start.next
            if start.next:
                start.next = start.next.next
            
                
        return head




