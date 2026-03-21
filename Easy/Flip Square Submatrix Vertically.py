class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for inc in range(k // 2):
            up, low = x + inc, x + k - inc - 1
            for col in range(y, y + k):
                grid[up][col], grid[low][col] = grid[low][col], grid[up][col]
        return grid
