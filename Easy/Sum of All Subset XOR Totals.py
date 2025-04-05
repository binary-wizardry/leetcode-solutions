from itertools import combinations, chain, accumulate
from operator import xor


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(xor, subset, 0) for subset in chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))


"""
Nice bit manipulation solition:

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums)-1)
"""
