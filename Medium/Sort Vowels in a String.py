class Solution:
    def sortVowels(self, s: str) -> str:
        vovels = {vovel: 0 for vovel in 'AEIOUaeiou'}
        counts = Counter(vovels)
        
        for char in s:
            if char in counts:
                counts[char] += 1
        
        vovels = counts.elements()
        return ''.join(next(vovels) if char in counts else char for char in s)
