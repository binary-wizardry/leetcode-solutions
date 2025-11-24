class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prefix = 0
        result = []
        for num in nums:
            prefix = (prefix << 1) + num
            result.append(not(prefix % 5))
        return result
