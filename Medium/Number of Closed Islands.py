class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def backtrack(i, j, color):
            if color == '⬛️':
                return
        
            grid[i][j] = '⬛️'
        
            for di, dj in moves:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and grid[x][y] == color:
                    backtrack(x, y, color)
    
        n, m = len(grid), len(grid[0])
        moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
        for i in range(n):
            backtrack(i, 0, grid[i][0])
            backtrack(i, m - 1, grid[i][m - 1])
        
        for j in range(m):
            backtrack(0, j, grid[0][j])
            backtrack(n - 1, j, grid[n - 1][j])
        
        count = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    count += 1
                    backtrack(i, j, grid[i][j])
    
        return count

# https://stepik.org/lesson/2259995/step/6?unit=2294013
