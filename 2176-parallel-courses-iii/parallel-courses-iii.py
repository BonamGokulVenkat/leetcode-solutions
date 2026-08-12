class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            indegree[v] += 1

        finish = time[:]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            u = queue.popleft()

            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + time[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        return max(finish)