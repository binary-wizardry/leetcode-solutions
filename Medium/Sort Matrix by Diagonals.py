class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for row in range(n):
            diag = sorted(grid[row + i][i] for i in range(n - row))
            for i in range(n - row):
                grid[row + i][i] = diag.pop()
        for col in range(1, n):
            diag = sorted((grid[i][col + i] for i in range(n - col)), reverse=True)
            for i in range(n - col):
                grid[i][col + i] = diag.pop()
        return grid
