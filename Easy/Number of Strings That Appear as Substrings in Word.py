class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(item in word for item in patterns)
