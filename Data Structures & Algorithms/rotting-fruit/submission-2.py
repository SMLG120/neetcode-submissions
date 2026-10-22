class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0

        # count number of fresh oranges and queue rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Return if outside range or is not fresh
                    if (row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                

        
