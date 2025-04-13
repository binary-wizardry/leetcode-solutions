class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, (n + 1) // 2, 10 ** 9 + 7) * pow(4, n // 2, 10 ** 9 + 7)) % (10 ** 9 + 7)

"""
n = 1 so index = 0 so we can have 02468 it means 5 combinations
n = 2 so index = 1 so we can have 2357 it means 5x4 combinatioins
n = 3 so index = 0 means 5x4x5 combinations
n = 4 so index = 1 means 5x4x5x4 combinations ...
"""
