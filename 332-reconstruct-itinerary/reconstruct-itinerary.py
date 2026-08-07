class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        tickets.sort(reverse=True)

        for src, dst in tickets:
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]