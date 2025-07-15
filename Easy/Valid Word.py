class Solution:
    def isValid(self, word: str) -> bool:
        VOVELS = 'aeiouAEIOU'
        has_vovel = any(c in VOVELS for c in word)
        
        CONSONANT = ''.join(set(string.ascii_letters) - set(VOVELS))
        has_consonant = any(c in CONSONANT for c in word)
        
        return len(word) > 2 and word.isalnum() and has_vovel and has_consonant
