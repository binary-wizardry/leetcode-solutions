class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if y > x:
            a, b = b, a
            x, y = y, x
        
        stack = []
        score = 0
        for c in s:
            stack.append(c)
            if len(stack) > 1 and stack[-2] == a and stack[-1] == b:
                stack.pop()
                stack.pop()
                score += x
        
        new_stack = []
        for c in stack:
            new_stack.append(c)
            if len(new_stack) > 1 and new_stack[-2] == b and new_stack[-1] == a:
                new_stack.pop()
                new_stack.pop()
                score += y

        return score
