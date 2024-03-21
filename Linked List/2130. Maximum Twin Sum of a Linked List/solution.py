# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        sums = []
        while head:
            sums.append(head.val)
            head = head.next
        ptr1 = 0
        ptr2 = len(sums)-1
        while ptr1<ptr2:
            maxSum = max(maxSum, sums[ptr1]+sums[ptr2])
            ptr1 += 1
            ptr2 -= 1
        return maxSum