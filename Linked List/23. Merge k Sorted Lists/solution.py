# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        h = []
        if len(lists)>0:
            count = 0
            for currList in lists:
                currNode = currList
                while currNode:
                    heapq.heappush(h,(currNode.val,count,currNode))
                    count += 1
                    currNode = currNode.next
        
        else:
            return None
        
        if h:
            prev = ans
            for _ in range(len(h)):
                prev.next = heapq.heappop(h)[2]
                prev = prev.next
            return ans.next
        else:
            return None