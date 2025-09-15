class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(set(word).isdisjoint(broken) for word in text.split())

#  checking with str without typecast into set is faster for this task kek
