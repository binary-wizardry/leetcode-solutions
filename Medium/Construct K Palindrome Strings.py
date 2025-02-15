from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        odd_counts = sum(count % 2 for count in Counter(s).values())
        if odd_counts > k:
            return False
        return True
