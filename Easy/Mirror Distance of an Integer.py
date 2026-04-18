class Solution:
    def reverse(self, n: int, result: int = 0) -> int:
        if not n:
            return result
        return self.reverse(n // 10, result * 10 + n % 10)

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
