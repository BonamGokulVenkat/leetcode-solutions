class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        ans = []

        while heap:
            count1, ch1 = heapq.heappop(heap)

            if len(ans) >= 2 and ans[-1] == ch1 and ans[-2] == ch1:

                if not heap:
                    break

                count2, ch2 = heapq.heappop(heap)

                ans.append(ch2)
                count2 += 1  
                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))

                heapq.heappush(heap, (count1, ch1))

            else:
                ans.append(ch1)
                count1 += 1

                if count1 < 0:
                    heapq.heappush(heap, (count1, ch1))

        return "".join(ans)