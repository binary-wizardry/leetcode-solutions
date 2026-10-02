class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def generate(current: str, opened: int, closed: int) -> None:
            if len(current) == n * 2:
                result.append(current)
                return
            
            if opened < n:
                generate(current + '(', opened + 1, closed)
            if opened > closed:
                generate(current + ')', opened, closed + 1)
        
        result = []
        generate('', 0, 0)
        return result
