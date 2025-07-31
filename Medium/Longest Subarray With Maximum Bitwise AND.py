class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_bitwise_and = max(nums)
        count = result = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] == max_bitwise_and:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result + 1
