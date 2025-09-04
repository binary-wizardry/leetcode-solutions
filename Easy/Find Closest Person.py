class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        time1, time2 = abs(z - x), abs(z - y)
        condition1 = time1 != time2
        condition2 = time1 > time2
        return condition1 + condition2
