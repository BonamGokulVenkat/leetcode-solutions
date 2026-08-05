class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            connected[u][v] = True
            connected[v][u] = True

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if connected[i][j]:
                    rank -= 1
                ans = max(ans, rank)

        return ans