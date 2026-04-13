class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        left = right = start
        while nums[left] != target and nums[right] != target:
            left = max(0, left - 1)
            right = min(n - 1, right + 1)
        
        if nums[left] == target:
            return start - left
        elif nums[right] == target:
            return right - start
