class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        prefix = sum(sum(row) for row in grid)
        
        row_prefix = accumulate(sum(row) for row in grid)
        for cur in row_prefix:
            if cur == prefix - cur:
                return True
        
        col_prefix = accumulate(sum(grid[i][j] for i in range(m)) for j in range(n))
        for cur in col_prefix:
            if cur == prefix - cur:
                return True
        
        return False
