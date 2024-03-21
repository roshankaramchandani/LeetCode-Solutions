# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = []
        result = 0
        while True:
            ans.append(head.val)
            if head.next == None:
                break
            head = head.next
        for i in range(len(ans)):
            result += ans[len(ans) - i - 1]*(2**i)
        return result
