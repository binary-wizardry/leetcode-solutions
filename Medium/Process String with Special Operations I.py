class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c in ascii_lowercase:
                result.append(c)
            elif c == '*':
                if result:
                    result.pop()
            elif c == '#':
                result *= 2
            elif c == '%':
                result = result[::-1]
        return ''.join(result)
