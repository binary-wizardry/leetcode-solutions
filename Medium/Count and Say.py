from itertools import groupby

class Solution:
    def rle(self, s: str) -> str:
        return ''.join(str(sum(1 for _ in group)) + str(x) for x, group in groupby(s))

    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = self.rle(s)
        return s
