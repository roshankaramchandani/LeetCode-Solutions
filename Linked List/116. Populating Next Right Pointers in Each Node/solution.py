"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def solve(curr):
            if not curr.left:
                return 
            curr.left.next = curr.right
            if curr.left.left:
                curr.left.right.next = curr.right.left 
                if curr.right.next:
                    curr.right.right.next = curr.right.next.left
            solve(curr.left)
            solve(curr.right)
            

        if root:
            solve(root)
        
        return root
