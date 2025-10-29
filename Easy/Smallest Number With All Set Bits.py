class Solution:
    def smallestNumber(self, n: int) -> int:
        return int(''.join('1' for bit in f'{n:b}'), 2)
