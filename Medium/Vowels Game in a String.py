class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return len(set(s) & set('aeiou')) > 0
