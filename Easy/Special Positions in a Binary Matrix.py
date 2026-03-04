class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ones_in_rows = [sum(row) for row in mat]
        ones_in_cols = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        return sum(ones_in_rows[i] == ones_in_cols[j] == mat[i][j] == 1 for i in range(m) for j in range(n))
