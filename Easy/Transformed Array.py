class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            index = (i + num) % n
            ans[i] = nums[index]
        return ans
