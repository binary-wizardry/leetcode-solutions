class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = sum(range(1, 2 * n, 2))
        sumEven = sum(range(2, 2 * n + 1, 2))
        return gcd(sumOdd, sumEven)
