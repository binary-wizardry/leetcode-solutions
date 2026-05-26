class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(c.upper() in word for c in set(filter(str.islower, word)))
