# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        tail = head
        while curr:
            n += 1
            if not curr.next:
                tail = curr
            curr = curr.next
        if n==0:
            return None
        rotate = k%n
        if rotate==0:
            return head
        rotate = n-rotate-1
        curr = head
        while rotate>0:
            curr = curr.next
            rotate -= 1
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
        