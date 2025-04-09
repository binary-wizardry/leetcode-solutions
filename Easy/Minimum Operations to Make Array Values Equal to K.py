class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = set()
        for n in nums:
            if n < k:
                return -1
            elif n > k and n not in operations:
                operations.add(n)
        return len(operations)
