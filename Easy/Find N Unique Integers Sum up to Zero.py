class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for num in range(1, n // 2 + 1):
            result.append(-num)
            result.append(num)
        if n % 2:
            result.append(0)
        return result
