class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n * m >> 1  # n * m // 2
