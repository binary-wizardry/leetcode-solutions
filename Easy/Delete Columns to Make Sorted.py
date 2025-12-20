class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in zip(*strs):
            for a, b in pairwise(col):
                if a > b:
                    count += 1
                    break
        return count
