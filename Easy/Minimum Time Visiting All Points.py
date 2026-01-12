class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for (x1, y1), (x2, y2) in pairwise(points):
            time += max(abs(x2 - x1), abs(y2 - y1))
        return time
