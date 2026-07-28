class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()

        for i in range(len(tickets)):
            q.append((i, tickets[i]))

        time = 0

        while q:
            idx, rem = q.popleft()
            rem -= 1
            time += 1

            if rem == 0:
                if idx == k:
                    return time
            else:
                q.append((idx, rem))