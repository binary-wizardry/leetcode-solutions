class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
