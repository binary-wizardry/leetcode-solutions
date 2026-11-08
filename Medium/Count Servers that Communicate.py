class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            count = 0
            queue = deque()
            queue.append((row, col))
            
            while queue:
                x, y = queue.popleft()
                
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                count += 1

                for dx in range(x + 1, n):
                    if grid[dx][y]:
                        queue.append((dx, y))
                        break
                for dx in range(x - 1, -1, -1):
                    if grid[dx][y] and (dx, y) not in visited:
                        queue.append((dx, y))
                        break

                for dy in range(y + 1, m):
                    if grid[x][dy]:
                        queue.append((x, dy))
                        break
                for dy in range(y - 1, -1, -1):
                    if grid[x][dy] and (x, dy) not in visited:
                        queue.append((x, dy))
                        break
            return count

        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count = bfs(i, j)
                    if count > 1:
                        result += count
        return result
