class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)

        # Add original index
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])

        new_edges.sort(key=lambda x: x[2])

        def kruskal(skip, force):
            dsu = DSU(n)
            weight = 0
            used = 0

            # Force include one edge
            if force != -1:
                u, v, w, _ = new_edges[force]
                dsu.union(u, v)
                weight += w
                used += 1

            for i, (u, v, w, _) in enumerate(new_edges):
                if i == skip:
                    continue

                if dsu.union(u, v):
                    weight += w
                    used += 1

            if used != n - 1:
                return float("inf")

            return weight

        mst_weight = kruskal(-1, -1)

        critical = []
        pseudo = []

        for i in range(m):
            # Check if edge is critical
            if kruskal(i, -1) > mst_weight:
                critical.append(new_edges[i][3])

            # Check if edge is pseudo-critical
            elif kruskal(-1, i) == mst_weight:
                pseudo.append(new_edges[i][3])

        return [critical, pseudo]