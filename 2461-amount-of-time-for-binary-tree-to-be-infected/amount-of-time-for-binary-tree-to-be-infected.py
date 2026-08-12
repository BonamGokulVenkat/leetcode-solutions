# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        start_node = None

        def build_parent(node, par=None):
            nonlocal start_node

            if not node:
                return

            if node.val == start:
                start_node = node

            if par:
                parent[node] = par

            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root)

        queue = deque([start_node])
        visited = {start_node}
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])

            minutes += 1

        return minutes