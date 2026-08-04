class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        minimum, maximum = min(nums), max(nums)
        return [num for num in range(minimum, maximum) if num not in nums]
