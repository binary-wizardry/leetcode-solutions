class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((int(log10(num)) + 1) % 2 == 0 for num in nums)
