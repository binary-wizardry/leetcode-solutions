class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        initial = complexity[0]
        for num in complexity[1:]:
            if num <= initial:
                return 0
        
        MOD = 10 ** 9 + 7
        count = 1
        for i in range(2, len(complexity)):
            count *= i
            count %= MOD
        return count
