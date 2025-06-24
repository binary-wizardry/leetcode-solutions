class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result, index = [], 0
        for i, num in enumerate(nums):
            if i - index > k:
                index += 1
            while num == key and index < len(nums) and abs(i - index) <= k:
                result.append(index)
                index += 1
        return result
