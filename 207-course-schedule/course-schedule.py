from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses


        def dfs(node):
            if state[node] == 1:
                return False     

            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True