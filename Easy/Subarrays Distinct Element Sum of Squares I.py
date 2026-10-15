class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            distincts = set()
            for j in range(i, len(nums)):
                distincts.add(nums[j])
                result += len(distincts) ** 2
        return result
