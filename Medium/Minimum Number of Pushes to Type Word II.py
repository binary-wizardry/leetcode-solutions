class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        result = increment = 0
        for i, (_, count) in enumerate(freq.most_common()):
            result += count * (i // 8 + 1)
        return result
