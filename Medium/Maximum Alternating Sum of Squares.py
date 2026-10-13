class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(nums, key=abs)
        result = 0
        
        if len(nums) % 2:
            appendix = nums.pop()
            result += appendix ** 2
        
        for i in range(len(nums) // 2):
            print(i)
            result += nums[~i] ** 2 - nums[i] ** 2
        
        return result
