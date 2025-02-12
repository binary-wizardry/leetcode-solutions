class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = sum(nums)
        for num in nums[:-1]:
            left += num
            right -= num
            if left >= right:
                count += 1
        return count
