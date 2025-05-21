class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row = any(not matrix[0][j] for j in range(n))
        first_col = any(not matrix[i][0] for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if not matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if not matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col:
            for i in range(m):
                matrix[i][0] = 0

# O(1) space complexity
