class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hash_table = {n: i for i, n in enumerate(sorted(set(arr)), 1)}
        return [hash_table[n] for n in arr]
