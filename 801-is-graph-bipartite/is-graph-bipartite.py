class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n 

        def dfs(node, curr_color):
            color[node] = curr_color

            for nei in graph[node]:
                if color[nei] == 0:
                    if not dfs(nei, -curr_color):
                        return False
                elif color[nei] == curr_color:
                    return False

            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False

        return True