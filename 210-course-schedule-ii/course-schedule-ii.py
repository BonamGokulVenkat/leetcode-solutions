class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for c,p in prerequisites:
            graph[p].append(c)
            indegree[c]+=1
        queue=deque(i for i in range(numCourses) if indegree[i]==0)
        ans=[]
        processed=0
        while queue:
            node=queue.popleft()
            ans.append(node)
            processed+=1
            for n in graph[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        return ans if processed==numCourses else []