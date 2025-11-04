class Solution:
    def XSum(self, nums: List[int], x: int) -> int:
        nums.sort(reverse=True)
        return sum(n * count for n, count in Counter(nums).most_common(x))

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        return [self.XSum(nums[i: i + k], x) for i in range(len(nums) - k + 1)]
