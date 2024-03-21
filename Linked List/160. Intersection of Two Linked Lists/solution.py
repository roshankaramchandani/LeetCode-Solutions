# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==headB:
            return headA
        ptrA = headA
        ptrB = headB
        lenA = 1
        lenB = 1
        while ptrA.next:
            ptrA = ptrA.next
            lenA += 1
        while ptrB.next:
            ptrB = ptrB.next
            lenB += 1
        
        if ptrA!=ptrB:
            return None
        print(ptrA == ptrB)

        newPtr = headA
        secPtr = headB
        
        if lenB>lenA:
            newPtr = headB
            secPtr = headA
        
        for _ in range(abs(lenA-lenB)):
            newPtr = newPtr.next
        
        while newPtr.next:
            if newPtr==secPtr:
                return newPtr
            newPtr = newPtr.next
            secPtr = secPtr.next
        return newPtr
        
        