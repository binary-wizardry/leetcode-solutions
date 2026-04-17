class Solution:
    def reverse(self, num: int, result: int=0) -> int:
        if not num:
            return result
        return self.reverse(num // 10, result * 10 + num % 10)

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        indexes = {}
        result = float('inf')
        for i, num in enumerate(nums):
            if num in indexes:
                result = min(result, i - indexes[num])
            indexes[self.reverse(num)] = i
        return -1 if result == float('inf') else result
