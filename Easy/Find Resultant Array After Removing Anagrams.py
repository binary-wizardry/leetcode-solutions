class Solution:
    def counter(self, word: str) -> str:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        return ''.join(str(n) for n in count)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ''
        for word in words:
            count = self.counter(word)
            if count != prev:
                result.append(word)
                prev = count
        return result
