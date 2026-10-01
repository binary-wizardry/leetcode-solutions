class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            elif not stack:
                return False
            else:
                prev = stack.pop()
                if prev != matching[bracket]:
                    return False
        return not stack
