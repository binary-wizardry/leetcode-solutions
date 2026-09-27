class Solution:
    def reverseParentheses(self, s: str) -> str:
        right = s.find(')')
        if right != -1:
            left = s.rfind('(', 0, right)
            reverse = s[:left] + s[right-1:left:-1] + s[right+1:]
            return self.reverseParentheses(reverse)
        return s
