class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        squares = set(i * i for i in range(1, n + 1))
        for a in range(3, n + 1):
            for b in range(a + 1, n + 1):
                c = a * a + b * b
                if c in squares:
                    count += 2
        return count
