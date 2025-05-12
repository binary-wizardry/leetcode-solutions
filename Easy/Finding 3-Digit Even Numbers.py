class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        return sorted(set(
            a * 100 + b * 10 + c
            for a, b, c in permutations(digits, 3)
            if a and c % 2 == 0))
