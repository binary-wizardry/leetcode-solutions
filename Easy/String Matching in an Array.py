class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        string = ' '.join(words)
        return [word for word in words if string.count(word) > 1]
