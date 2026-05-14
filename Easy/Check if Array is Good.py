class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i, num in enumerate(nums, 1):
            if i != num and i != len(nums):
                return False
        return nums[-1] == len(nums) - 1
