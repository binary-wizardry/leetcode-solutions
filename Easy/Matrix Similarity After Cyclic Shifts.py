class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n

        rotate = [deque(row) for row in mat]
        for i in range(m):
            if i % 2 == 0:
                rotate[i].rotate(-k)
            else:
                rotate[i].rotate(k)
        
        rotate = [list(row) for row in rotate]
        return rotate == mat
