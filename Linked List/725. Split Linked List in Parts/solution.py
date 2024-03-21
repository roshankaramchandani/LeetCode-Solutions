# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        ans = [None]*k
        if length==0:
            return ans
        perPart = length//k
        remainder = length%k

        currHead = head
        ptr = ListNode(val=0,next=head)
        for i in range(len(ans)):
            if not ptr:
                break
            count = perPart
            if remainder>0:
                count += 1
                remainder -= 1
            
            for _ in range(count):
                ptr = ptr.next
            newHead = ptr.next
            ptr.next = None
            ans[i] = currHead
            currHead = newHead
            ptr = ListNode(val=0,next=currHead)



        return ans



