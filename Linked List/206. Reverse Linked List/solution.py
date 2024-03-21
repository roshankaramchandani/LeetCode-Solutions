# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                sec = head.next
            else:
                return head
            head.next = None
            while True:
                try:
                    temp = sec.next
                    sec.next = head
                except:
                    break
                head = sec
                sec = temp
            return head

        else:
            return head
