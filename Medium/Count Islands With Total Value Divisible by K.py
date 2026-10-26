class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        def bfs(row, col):
            stack = deque()
            stack.append((row, col))
            count = 0

            while stack:
                x, y = stack.pop()
                
                if 0 <= x < n and 0 <= y < m and grid[x][y]:
                    count += grid[x][y]
                    grid[x][y] = None
                    for dx, dy in moves:
                        stack.append((x + dx, y + dy))
            
            return count

        n, m = len(grid), len(grid[0])
        moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count = bfs(i, j)
                    res += not count % k
        
        return res
