class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        missed = stack = 0
        for bracket in s:
            if bracket == '(':
                stack += 1
            elif stack: 
                stack -= 1
            else:               # bracket == ')' and stack == []
                missed += 1
        return stack + missed
