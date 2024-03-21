# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head.next
            repeat = head.val
            first = False
            prev = head
            while curr:
                if curr.val == repeat:
                    if first:
                        first = False
                    else:
                        prev.next = curr.next
                        curr = curr.next
                        continue
                else:
                    repeat = curr.val
                    first = True
                    continue
                curr = curr.next
                prev = prev.next           
                
        return head

