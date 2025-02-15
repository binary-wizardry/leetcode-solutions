class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0][1:])
        bottom_sum = 0
        optimal_result = max(top_sum, bottom_sum)
        for i in range(len(grid[0]) - 1):
            top_sum -= grid[0][i + 1]
            bottom_sum += grid[1][i]
            result = max(top_sum, bottom_sum)
            if result <= optimal_result:
                optimal_result = result
            else:
                break
        return optimal_result
