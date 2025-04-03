class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_a, max_ab, result = 0, 0, 0
        for num in nums:
            result = max(result, max_ab * num)
            max_ab = max(max_ab, max_a - num)
            max_a = max(max_a, num)
        return result
