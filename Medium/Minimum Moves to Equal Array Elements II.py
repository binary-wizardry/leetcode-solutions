class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mid = median_low(nums)
        return sum(abs(mid - n) for n in nums)

# https://stepik.org/lesson/1481818/step/5?unit=1501531
