class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visit = set()
        
        def checkNeighbour(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return 1 + checkNeighbour(r + 1, c) + checkNeighbour(r - 1, c) + checkNeighbour(r, c + 1) + checkNeighbour(r, c - 1)

        count = 0
        for i in range(n):
            for j in range(m):
                cur = grid[i][j]
                # if it is an island
                if grid[i][j] == 1:
                    count = max(count, checkNeighbour(i, j))
        return count

    
        
                