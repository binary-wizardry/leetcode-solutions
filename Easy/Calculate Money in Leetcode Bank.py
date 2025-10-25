class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        day = week = 0
        while n:
            if not day % 7:
                week += 1
                day = 0
            total += week + day
            day += 1
            n -= 1
        return total
