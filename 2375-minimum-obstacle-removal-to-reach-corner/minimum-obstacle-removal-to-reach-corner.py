class Solution:
    def minimumObstacles(self, grid):
        m = len(grid)
        n = len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while dq:
            r, c = dq.popleft()

            if r == m - 1 and c == n - 1:
                return dist[r][c]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    cost = grid[nr][nc]
                    new_dist = dist[r][c] + cost

                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist

                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[m - 1][n - 1]