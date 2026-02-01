class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2, min3 = inf, inf, nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return min1 + min2 + min3
