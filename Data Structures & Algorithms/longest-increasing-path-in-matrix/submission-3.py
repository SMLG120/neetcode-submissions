class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        # patter: dfs + memoization
        # dp[(r, c)] = longest path starting at (r, c)

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            # current cell counts as length 1
            best = 1
            # pattern: grid traversal in 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # pattern: boundary + strictly increasing check
                if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))
            # pattern: store result before returnign
            dp[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))

            