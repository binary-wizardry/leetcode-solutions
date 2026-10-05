class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []

        for bracket in s:
            if bracket == '(':
                stack.append(0)
            else:
                prev = stack.pop()
                count = 1 if not prev else prev * 2
                if stack:
                    stack[-1] += count
                else:
                    score += count

        return score
