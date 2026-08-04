class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True

            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    dfs(nei)

        provinces = 0

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces