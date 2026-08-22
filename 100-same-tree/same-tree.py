# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d1=deque()
        d2=deque()
        
        d1.append(p)
        d2.append(q)
        while d1 and d2:
            node1=d1.popleft()
            node2=d2.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val!=node2.val:
                return False
            d1.append(node1.left)
            d1.append(node1.right)
            d2.append(node2.left)
            d2.append(node2.right)
            
            
        return True