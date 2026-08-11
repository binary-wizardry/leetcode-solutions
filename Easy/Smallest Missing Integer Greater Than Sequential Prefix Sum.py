class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = 0
        delta = nums[0]
        for i, num in enumerate(nums):
            if num - i != delta:
                break
            prefix += num
        
        while prefix in nums:
            prefix += 1
        
        return prefix
