class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
# The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it
