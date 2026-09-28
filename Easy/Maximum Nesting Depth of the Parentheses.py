class Solution:
    def counter(self, count: int, char: str) -> int:
        return count + 1 if char == '(' else count - 1 if char == ')' else count
    
    def maxDepth(self, s: str) -> int:
        return max(accumulate(s, self.counter, initial=0))
        
