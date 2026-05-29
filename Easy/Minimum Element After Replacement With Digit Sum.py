class Solution:
    def sum_digits(self, num: int) -> int:
        return num % 10 + self.sum_digits(num // 10) if num else 0

    def minElement(self, nums: List[int]) -> int:
        return min(self.sum_digits(num) for num in nums)
