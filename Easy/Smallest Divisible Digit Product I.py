class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for number in count(n):
            
            mul, n = 1, number
            while n:
                digit, n = n % 10, n // 10
                mul *= digit

            if not mul % t:
                return number
