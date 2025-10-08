class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        n = len(potions)
        for spell in spells:
            power = success / spell
            result.append(n - bisect_left(potions, power))
        return result
