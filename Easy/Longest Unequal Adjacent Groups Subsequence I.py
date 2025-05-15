class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(groups)):
            if groups[i - 1] != groups[i]:
                result.append(words[i])
        return result
