class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for dist in range(n):
            left = (startIndex - dist + n) % n
            right = (startIndex + dist) % n
            if words[left] == target or words[right] == target:
                return dist
        return -1
