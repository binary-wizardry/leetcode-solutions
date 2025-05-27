class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return 2 * sum(num for num in range(1, n + 1) if num % m) - n * (n + 1) // 2
