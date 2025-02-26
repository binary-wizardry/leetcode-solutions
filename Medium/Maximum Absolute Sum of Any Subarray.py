class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix sum
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)
        return max(prefix_sum) - min(prefix_sum)
