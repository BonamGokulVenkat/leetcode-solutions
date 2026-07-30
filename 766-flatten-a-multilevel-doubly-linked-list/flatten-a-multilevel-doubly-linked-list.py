"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            curr = node
            last = None

            while curr:
                nxt = curr.next

                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    # Insert child list
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    # Connect child tail with original next
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    last = child_tail
                    curr = nxt
                else:
                    last = curr
                    curr = curr.next

            return last

        if head:
            dfs(head)

        return head