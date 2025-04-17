class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i] == nums[j] and not (i * j) % k for i, j in itertools.combinations(range(len(nums)), 2))
