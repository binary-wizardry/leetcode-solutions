class Solution:
    def invert(self, s: str) -> str:
        return ''.join('0' if c == '1' else '1' for c in s)
    
    def rec(self, n: int) -> str:
        if n == 1:
            return '0'
        prev = self.rec(n - 1)
        return prev + '1' + self.invert(prev)[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        return self.rec(n)[k - 1]
