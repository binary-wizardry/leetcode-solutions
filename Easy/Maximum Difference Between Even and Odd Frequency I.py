class Solution:
    def maxDifference(self, s: str) -> int:
        counts = [0] * 26
        for char in s:
           counts[ord(char) - ord('a')] += 1

        return max(n for n in counts if n % 2) - min(n for n in counts if n and n % 2 == 0)
