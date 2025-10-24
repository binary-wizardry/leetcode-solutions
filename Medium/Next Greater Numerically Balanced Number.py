class Solution:
    def balanced(self, n: int) -> bool:
        n = str(n)
        if '0' in n or '7' in n or '8' in n or '9' in n:
            return False
        for digit in set(n):
            if int(digit) != n.count(digit):
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            if self.balanced(n):
                return n
