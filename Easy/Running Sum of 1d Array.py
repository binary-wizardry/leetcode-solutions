from itertools import accumulate
from operator import add


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums, add))
# prefix sum
