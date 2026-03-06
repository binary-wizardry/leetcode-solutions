class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not '1' in s.lstrip('1')
