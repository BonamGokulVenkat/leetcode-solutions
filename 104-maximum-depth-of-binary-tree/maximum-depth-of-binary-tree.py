# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.helper(root,0)
    def helper(self,root: TreeNode | None,count: int)-> int:
        if root==None:
            return count
        left=self.helper(root.left,count+1)
        right=self.helper(root.right,count+1)
        return max(left,right)