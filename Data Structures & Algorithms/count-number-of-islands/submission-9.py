class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nc < 0 or nc == cols or nr < 0 or nr == rows or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1
        return numIslands