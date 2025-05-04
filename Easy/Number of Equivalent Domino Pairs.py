class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashmap = Counter(tuple(sorted(domino)) for domino in dominoes)
        return sum(count * (count - 1) // 2 for count in hashmap.values())
