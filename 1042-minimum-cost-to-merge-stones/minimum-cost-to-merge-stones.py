class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        @lru_cache(None)
        def dp(i, j, piles):
            if i == j:
                return 0 if piles == 1 else float("inf")

            if piles == 1:
                return dp(i, j, k) + prefix[j + 1] - prefix[i]

            ans = float("inf")

            for mid in range(i, j, k - 1):
                ans = min(
                    ans,
                    dp(i, mid, 1) + dp(mid + 1, j, piles - 1)
                )

            return ans

        return dp(0, n - 1, 1)