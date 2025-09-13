class Solution:
    def maxFreqSum(self, s: str) -> int:
        vovels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        cnt_vovels = [0] * 5
        cnt_consonants = [0] * 21
        for c in s:
            if c in vovels:
                cnt_vovels[vovels.index(c)] += 1
            else:
                cnt_consonants[consonants.index(c)] += 1
        return max(cnt_vovels) + max(cnt_consonants)
