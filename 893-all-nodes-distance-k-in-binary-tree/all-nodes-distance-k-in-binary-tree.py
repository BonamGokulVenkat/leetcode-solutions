# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent = {}

        def build_parent(node, par=None):
            if not node:
                return

            parent[node] = par

            build_parent(node.left, node)
            build_parent(node.right, node)

        build_parent(root)

        queue = deque([target])
        visited = {target}

        distance = 0

        while queue:

            if distance == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])

            distance += 1

        return []