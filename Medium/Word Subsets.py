class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hash_table = {}
        for word in words2:
            for letter in word:
                hash_table[letter] = max(hash_table.get(letter, 0), word.count(letter))
        print(hash_table)
        result = []
        for word in words1:
            if all(map(lambda letter, count: word.count(letter) >= count, hash_table, hash_table.values())):
                result.append(word)
        return result
