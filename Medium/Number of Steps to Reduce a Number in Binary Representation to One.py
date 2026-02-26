class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != '1':
            steps += 1
            
            if s[-1] == '0':
                s = s[:-1]
            else:
                i = len(s) - 1
                while s[i] == '1' and i > 0:
                    i -= 1
                s = s[:i] + '1' + '0' * (len(s) - 1 - (i if i else -1))

        return steps
