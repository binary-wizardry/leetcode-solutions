class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for char in s:
            if not result or len(result) == 1:
                result.append(char)
                continue
            
            if char != result[-1] or char != result[-2]:
                result.append(char)
        
        return ''.join(result)
