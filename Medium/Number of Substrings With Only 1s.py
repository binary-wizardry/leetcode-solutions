class Solution:
    def numSub(self, s: str) -> int:
        result = sequence = 0
        for n in s:
            if n == '1':
                sequence += 1
                result += sequence
            else:
                sequence = 0
        return result % (10 ** 9 + 7)
