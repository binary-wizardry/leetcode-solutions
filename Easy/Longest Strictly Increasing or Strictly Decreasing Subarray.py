class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        streak = monotonic = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                streak += 1
            else:
                streak = 1
            monotonic = max(monotonic, streak)
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                streak += 1
            else:
                streak = 1
            monotonic = max(monotonic, streak)
        return monotonic
