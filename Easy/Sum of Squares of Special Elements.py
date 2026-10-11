class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(n ** 2 for i, n in enumerate(nums, 1) if len(nums) % i == 0)
