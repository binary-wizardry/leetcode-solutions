class Solution:
    def binaryGap(self, n: int) -> int:
        ones = [i for i, bit in enumerate(f'{n:b}') if bit == '1']
        return max((b - a for a, b in pairwise(ones)), default=0)
