class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        discovery = [0] * n
        low = [0] * n
        parent = [-1] * n
        time = 0
        result = []
        
        def dfs(u):
            nonlocal time
            visited[u] = True
            discovery[u] = low[u] = time
            time += 1
            
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)
                    
                    
                    low[u] = min(low[u], low[v])
                    
                    
                    if low[v] > discovery[u]:
                        result.append([u, v])
                
                elif v != parent[u]:
                    
                    low[u] = min(low[u], discovery[v])
        
       
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return result