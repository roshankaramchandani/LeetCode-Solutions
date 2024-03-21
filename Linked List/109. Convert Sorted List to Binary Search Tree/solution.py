# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        def solve(left,right):
            if left>right:
                return None
            
            mid = left+(right-left)//2
            currRoot = TreeNode(arr[mid])
            if left<right:
                currRoot.left = solve(left,mid-1)
                currRoot.right = solve(mid+1,right)
            return currRoot

        return solve(0,len(arr)-1)