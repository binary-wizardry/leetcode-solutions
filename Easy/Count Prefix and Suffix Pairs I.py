class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        return sum(self.isPrefixAndSuffix(words[i], words[j]) for i in range(n) for j in range(i + 1, n))

    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)
