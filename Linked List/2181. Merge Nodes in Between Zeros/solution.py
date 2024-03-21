# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        new = head
        sum = 0
        while curr:
            if curr.val != 0:
                sum += curr.val
            else:
                curr.val = sum
                new.next = curr
                new = new.next
                sum = 0
            curr = curr.next
        head = head.next
        return head


            
