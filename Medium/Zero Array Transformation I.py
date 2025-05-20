class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffs = [0] * (len(nums) + 1)
        for a, b in queries:
            diffs[a] -= 1
            diffs[b + 1] += 1
        
        for num, diff in zip(nums, accumulate(diffs)):
            if num + diff > 0:
                return False
        return True
