class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 2 ** (int(log2(n)) + 1) - n - 1 if n else 1
