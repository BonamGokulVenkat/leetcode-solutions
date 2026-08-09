class Solution:
    def secondMinimum(self, n, edges, time, change):
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dist = [[float('inf'), float('inf')] for _ in range(n + 1)]

        pq = [(0, 1)]
        dist[1][0] = 0

        while pq:
            current, u = heapq.heappop(pq)

            for v in graph[u]:

                next_time = current

                phase = next_time % (2 * change)

                if phase >= change:
                    next_time += 2 * change - phase

                next_time += time

                if next_time < dist[v][0]:
                    dist[v][1] = dist[v][0]
                    dist[v][0] = next_time
                    heapq.heappush(pq, (next_time, v))

                elif dist[v][0] < next_time < dist[v][1]:
                    dist[v][1] = next_time
                    heapq.heappush(pq, (next_time, v))

                if dist[n][1] != float('inf'):
                    return dist[n][1]