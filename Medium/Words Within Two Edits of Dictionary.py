class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                count = 0
                for i, char in enumerate(word):
                    if query[i] != char:
                        count += 1
                if count <= 2:
                    result.append(query)
                    break
        return result
