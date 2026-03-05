class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum(a != b for a, b in zip(s, cycle('01'))), sum(a != b for a, b in zip(s, cycle('10'))))
