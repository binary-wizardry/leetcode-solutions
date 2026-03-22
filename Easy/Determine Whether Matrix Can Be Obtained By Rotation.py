class Solution:
    def right(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix[::-1])]

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            mat = self.right(mat)
            if mat == target:
                return True
        return False
