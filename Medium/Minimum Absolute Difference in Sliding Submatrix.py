class Solution:
    def min_diff(self, row: int, col: int, grid: List[List[int]], k: int) -> int:
        items = sorted(set(grid[i][j] for i in range(row, row + k) for j in range(col, col + k)))
        print(items)
        return min((abs(b - a) for a, b in pairwise(items)), default=0)

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                ans[i][j] = self.min_diff(i, j, grid, k)
        return ans
