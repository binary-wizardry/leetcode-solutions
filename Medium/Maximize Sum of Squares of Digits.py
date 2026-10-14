class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        result = []
        cur_sum = 0

        while num:
            digit = min(9, sum)
            num -= 1
            sum -= digit
            result.append(digit)
        
        return ''.join(map(str, result)) if not sum else ''
        
