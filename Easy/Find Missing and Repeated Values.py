class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        all_numbers = set(range(1, n ** 2 + 1))
        hash_numbers = set()
        for i in range(n):
            for j in range(n):
                number = grid[i][j]
                if number in hash_numbers:
                    a = number  # repeating number
                hash_numbers.add(number)
        (b, ) = all_numbers - hash_numbers  # missing number
        return [a, b]
