class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        n = min(arrLen, steps // 2 + 1)

        @lru_cache(None)
        def dp(pos, step):
            if pos < 0 or pos >= n:
                return 0

            if step == 0:
                return 1 if pos == 0 else 0

            return (
                dp(pos, step - 1) +
                dp(pos - 1, step - 1) +
                dp(pos + 1, step - 1)
            ) % MOD

        return dp(0, steps)