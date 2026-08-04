class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(curr, target, visited, product):
            if curr == target:
                return product

            visited.add(curr)

            for nei, weight in graph[curr]:
                if nei not in visited:
                    ans = dfs(nei, target, visited, product * weight)
                    if ans != -1:
                        return ans

            return -1

        res = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                res.append(-1.0)
            elif src == dst:
                res.append(1.0)
            else:
                res.append(dfs(src, dst, set(), 1.0))

        return res