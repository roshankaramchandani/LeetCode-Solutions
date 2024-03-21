# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverse(slow.next)
        slow.next = None
        current1 = head
        current2 = mid
        while current1:
            try:
                temp = current2.next
                current2.next = current1.next
                current1.next = current2
                current1 = current1.next.next
                current2 = temp
            except:
                break


    def reverse(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


            
        
            
            