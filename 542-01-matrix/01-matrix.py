class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows=len(mat)
        cols=len(mat[0])
        dist=[[-1]*cols for _ in range(rows)]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    dist[r][c]=0
                    q.append((r,c))
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if(0<=nr<rows and
                   0<=nc<cols and
                   dist[nr][nc]==-1):
                   dist[nr][nc]=1+dist[r][c]
                   q.append((nr,nc))
        return dist
            
