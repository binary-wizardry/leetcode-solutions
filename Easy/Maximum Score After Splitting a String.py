class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s[0] == '0'
        ones = s[1:].count('1')
        result = zeros + ones
        for number in s[1:-1]:
            if int(number):
                ones -= 1
            else:
                zeros += 1
            result = max(result, zeros + ones)
        return result
