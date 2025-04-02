class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_ab = 0
        max_a = 0
        result = 0
        for num in nums:
            result = max(result, max_ab * num)
            max_ab = max(max_ab, max_a - num)
            max_a = max(max_a, num)
        return result
