# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = False
        ptr1 = l1
        ptr2 = l2
        ans = None
        ptr3 = None
        while ptr1 and ptr2:
            temp = ptr1.val + ptr2.val + int(carry)
            if temp>9:
                temp %= 10
                carry = True
            else:
                carry = False
            if ptr1 == l1:
                ans = ListNode(temp)
                ptr3 = ans
            else:
                ptr3.next = ListNode(temp)
                ptr3 = ptr3.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if ptr1:
            while ptr1:
                temp = ptr1.val + int(carry)
                if temp>9:
                    temp %= 10
                    carry = True
                else:
                    carry = False
                ptr3.next = ListNode(temp)
                ptr1 = ptr1.next
                ptr3 = ptr3.next
        if ptr2:
            while ptr2:
                temp = ptr2.val + int(carry)
                if temp>9:
                    temp %= 10
                    carry = True
                else:
                    carry = False
                ptr3.next = ListNode(temp)
                ptr2 = ptr2.next
                ptr3 = ptr3.next
        if carry:
            ptr3.next = ListNode(1)
        return ans
                
