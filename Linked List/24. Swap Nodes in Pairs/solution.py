# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode(-1)
        start.next = head
        currN = head
        prevN = start

        while currN and currN.next:
            nextN = currN.next
            prevN.next = currN.next
            currN.next = nextN.next
            nextN.next = currN

            currN = currN.next
            prevN = nextN.next
        return start.next

            