class Solution:
    def checkString(self, s: str) -> bool:
        return s.rfind('a') < s.find('b') or 'b' not in s
