class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = log(1 << 31, 3) // 1  # 3 ** power <= 2 ** 31
        N = pow(3, power)  # N is max power of 3 for this problem
        return n > 0 and N % n == 0  # it works because 3 is prime
