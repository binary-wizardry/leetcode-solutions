class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hash_table = set()
        result = 0
        for num in nums:
            if num not in hash_table and num > 0:
                result += num
                hash_table.add(num)
        return result or max(nums)
