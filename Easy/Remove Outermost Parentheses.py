class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        is_outer = True

        for bracket in s:
            
            if is_outer:
                if bracket == '(':
                    is_outer = False
            
            else:
                if bracket == '(':
                    stack.append(bracket)
                    result.append(bracket)
                else:
                    if stack:
                        stack.pop()
                        result.append(bracket)
                    else:
                        is_outer = True
        
        return ''.join(result)
