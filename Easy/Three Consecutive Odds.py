class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        streak = 0
        for n in arr:
            if n % 2:
                streak += 1
                if streak == 3:
                    return True
            else:
                streak = 0
        return False
