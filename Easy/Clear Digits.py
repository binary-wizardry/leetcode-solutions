class Solution:
    def clearDigits(self, s: str) -> str:
        stack = collections.deque()
        for char in s:
            if char.isdigit():
                stack.pop() if stack else None
            else:
                stack.append(char)
        return ''.join(stack)
