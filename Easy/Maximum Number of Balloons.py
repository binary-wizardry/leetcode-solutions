class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        counts = Counter(text)
        return min(counts[char] // count for char, count in balloon.items())
