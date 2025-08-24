class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(nums):
            return len(nums) - 1
        left = 0
        zero_index = -1
        longest = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                longest = max(longest, right - 1 - left)
                left, zero_index = zero_index + 1, right
        longest = max(longest, right - left)
        return longest
