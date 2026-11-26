class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        state=[0]*numCourses
        for c,p in prerequisites:
            graph[p].append(c)
        ans=[]
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for n in graph[node]:
                if not dfs(n):
                    return False
            state[node]=2
            ans.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans[::-1]