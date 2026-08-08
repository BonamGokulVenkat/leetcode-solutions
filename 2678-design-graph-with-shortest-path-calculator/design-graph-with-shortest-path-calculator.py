class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * len(self.graph)
        dist[node1] = 0

        pq = [(0, node1)]

        while pq:
            cost, node = heapq.heappop(pq)

            if node == node2:
                return cost

            if cost > dist[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_cost = cost + weight

                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))

        return -1