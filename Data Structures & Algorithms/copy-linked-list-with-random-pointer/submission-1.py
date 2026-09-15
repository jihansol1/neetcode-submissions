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

        # go through the original linked list
        # map original nodes to copied nodes
        # assign random pointers in order

        curr = head
        newHead = Node(0)
        dummy = newHead
        m = {} # maps original node : copied node

        # first pass: create copied nodes and map original nodes with copied nodes
        while curr:
            # create copy of original node
            copy = Node(curr.val)
            # map og node with copied node
            m[curr] = copy
            dummy.next = copy
            curr = curr.next
            dummy = copy

        curr = head
        # second pass: add random pointers 
        while curr:
            copy = m[curr]
            if curr.random:
                copy.random = m[curr.random]
            else:
                copy.random = None
            
            curr = curr.next

            
        return newHead.next

            
            
            