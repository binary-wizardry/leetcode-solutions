class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mul, nums = 1, set(nums)
        while True:
            if k * mul not in nums:
                return k * mul
            mul += 1
