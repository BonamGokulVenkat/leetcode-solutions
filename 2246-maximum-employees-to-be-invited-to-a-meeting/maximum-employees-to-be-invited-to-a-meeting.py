class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n

        for i in range(n):
            indegree[favorite[i]] += 1

        depth = [1] * n
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            nxt = favorite[node]

            depth[nxt] = max(depth[nxt], depth[node] + 1)
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                queue.append(nxt)

        max_cycle = 0
        pair_sum = 0

        for i in range(n):
            if indegree[i] > 0:
                length = 0
                node = i

                while indegree[node] > 0:
                    indegree[node] = 0
                    length += 1
                    node = favorite[node]

                if length == 2:
                    j = favorite[i]
                    pair_sum += depth[i] + depth[j]
                else:
                    max_cycle = max(max_cycle, length)

        return max(max_cycle, pair_sum)