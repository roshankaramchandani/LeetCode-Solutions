# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr1 = list1
        ptr2 = list2

        ctr1 = 0
        while ctr1<a-1:
            ptr1 = ptr1.next
            ctr1 += 1
        
        change = ptr1

        while ctr1<=b:
            ptr1 = ptr1.next
            ctr1 += 1

        change.next = ptr2
        while ptr2.next:
            ptr2 = ptr2.next
        
        ptr2.next = ptr1

        return list1

        