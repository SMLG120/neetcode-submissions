class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search with matrices rows and cols
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        # perform binary search in rows
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1 # move down the cells
            elif target < matrix[row][0]:
                bot = row - 1 # move up the cells
            else:
                break # target must be in this row, stop
        
        if not (top <= bot):
            return False

        row = (top + bot) // 2 # now we know our corresponding row
        l, r = 0, COLS - 1
        # perform binary search in cols
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
            

        