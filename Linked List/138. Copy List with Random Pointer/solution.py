"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        links = {}
        current = head
        while current:
            links[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            if current.next:
                links[current].next = links[current.next]
            if current.random:
                links[current].random = links[current.random]
            current = current.next
        head1 = links[head]
        return head1
