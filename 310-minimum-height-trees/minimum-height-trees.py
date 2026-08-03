from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initial leaves
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        remaining = n

        while remaining > 2:
            size = len(q)
            remaining -= size

            for _ in range(size):
                leaf = q.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        q.append(neighbor)

        return list(q)