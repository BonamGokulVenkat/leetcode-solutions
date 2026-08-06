class Solution:
    def longestCycle(self, edges):
        n = len(edges)

        visited = [False] * n
        ans = -1

        for i in range(n):

            if visited[i]:
                continue

            path = {}
            node = i
            step = 0

            while node != -1 and not visited[node]:
                visited[node] = True
                path[node] = step
                step += 1
                node = edges[node]

            if node != -1 and node in path:
                ans = max(ans, step - path[node])

        return ans