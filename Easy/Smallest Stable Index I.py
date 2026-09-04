class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_min = list(accumulate(reversed(nums), min))
        prefix_max = accumulate(nums, max)

        for i, (cur_max, cur_min) in enumerate(zip(prefix_max, reversed(prefix_min))):
            if cur_max - cur_min <= k:
                return i
        
        return -1
