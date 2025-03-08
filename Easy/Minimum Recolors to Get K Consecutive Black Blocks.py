class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return min((blocks[i:i + k].count('W') for i in range(len(blocks) - k + 1)))
