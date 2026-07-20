class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        pal = [[False] * n for _ in range(n)]
        dp = [0] * n

        for i in range(n):
            dp[i] = i

            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 2 or pal[j + 1][i - 1]):
                    pal[j][i] = True

                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]