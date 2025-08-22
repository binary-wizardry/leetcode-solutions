class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        max_x = max_y = 0
        min_x = min_y = 1000
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    if row > max_x:
                        max_x = row
                    if row < min_x:
                        min_x = row
                    if col > max_y:
                        max_y = col
                    if col < min_y:
                        min_y = col
        dx, dy = max_x - min_x + 1, max_y - min_y + 1
        return dx * dy
