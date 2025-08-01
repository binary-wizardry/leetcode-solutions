class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(numRows - 1):
            row = [1]
            for a, b in pairwise(pascal[-1]):
                row.append(a + b)
            row.append(1)
            pascal.append(row)
        return pascal
