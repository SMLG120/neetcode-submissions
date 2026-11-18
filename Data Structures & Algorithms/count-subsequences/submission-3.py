class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0
        dp = [[-1] * (m + 1) for _ in range(n)]

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = dfs(i + 1, j) + dfs(i + 1, j + 1)
            else:
                dp[i][j] = dfs(i + 1, j)
            return dp[i][j]

        return dfs(0, 0)