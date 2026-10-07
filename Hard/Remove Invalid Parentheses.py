class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # ez bruteforce
        def backtrack(i, current, opened, closed, removed):
            if i == len(s):
                if opened == closed:
                    result.append([removed, current])
                return
            
            if s[i] == '(':
                backtrack(i + 1, current, opened, closed, removed + 1)
                backtrack(i + 1, current + '(', opened + 1, closed, removed)
            elif s[i] == ')':
                backtrack(i + 1, current, opened, closed, removed + 1)
                if opened > closed:
                    backtrack(i + 1, current + ')', opened, closed + 1, removed)
            else:
                backtrack(i + 1, current + s[i], opened, closed, removed)
        
        result = []
        backtrack(0, '', 0, 0, 0)
        optimal = min(removed for removed, _ in result)
        return list(set(seq for removed, seq in result if removed == optimal))
