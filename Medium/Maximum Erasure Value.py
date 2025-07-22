class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash_table = set()
        score = max_score = left = 0
        for num in nums:
            while num in hash_table:
                hash_table.remove(nums[left])
                score -= nums[left]
                left += 1
            hash_table.add(num)
            score += num
            max_score = max(score, max_score)
        return max_score
