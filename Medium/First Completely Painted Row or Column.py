class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [n] * m
        col = [m] * n
        d = dict()
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        for i, number in enumerate(arr):
            r, c = d[number]
            row[r] -= 1
            col[c] -= 1
            if not row[r] or not col[c]:
                return i
