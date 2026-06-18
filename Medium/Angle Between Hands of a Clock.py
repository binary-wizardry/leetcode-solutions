class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour * 30 + minutes * 0.5    # in degrees
        minutes *= 6                        # in degrees
        a, b = max(hour, minutes), min(hour, minutes)
        return min(a - b, 360 - a + b)
