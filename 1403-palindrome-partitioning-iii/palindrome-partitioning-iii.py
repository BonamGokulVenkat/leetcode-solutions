class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = (cost[i + 1][j - 1] if i + 1 <= j - 1 else 0) + (s[i] != s[j])

        @cache
        def dfs(i, parts):
            if n - i == parts:
                return 0
            if parts == 1:
                return cost[i][n - 1]

            ans = float("inf")

            for j in range(i, n - parts + 1):
                ans = min(ans, cost[i][j] + dfs(j + 1, parts - 1))

            return ans

        return dfs(0, k)