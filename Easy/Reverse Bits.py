class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(reversed(f'{n:0=32b}')), 2)
