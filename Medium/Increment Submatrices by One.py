class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for row in range(row1, row2 + 1):
                prefix[row][col1] += 1
                if col2 < n - 1:
                    prefix[row][col2 + 1] -= 1
        for i in range(n):
            for j in range(1, n):
                prefix[i][j] += prefix[i][j - 1]
        return prefix
