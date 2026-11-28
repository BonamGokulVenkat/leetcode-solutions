class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque([(0,0)])
        dp=[[float("inf")]*n for _ in range(m)]
        dp[0][0]=0
        directions=[
            (0,1),(1,0),(0,-1),(-1,0)
        ]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if 0<=nr<m and 0<=nc<n:
                    cost=grid[nr][nc]
                    new_cost=dp[r][c]+cost
                    if new_cost<dp[nr][nc]:
                        dp[nr][nc]=new_cost
                        if cost==0:
                            queue.appendleft((nr,nc))
                        else:
                            queue.append((nr,nc))
        return dp[m-1][n-1]