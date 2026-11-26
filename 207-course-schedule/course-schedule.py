class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        state=[0]*numCourses
        for c,p in prerequisites:
            graph[p].append(c)
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for i in graph[node]:
                if not dfs(i):
                    return False
            state[node]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True