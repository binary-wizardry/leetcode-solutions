class Solution:
    def side_length(self, p1: list[int, int], p2: list[int, int]) -> float:
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            a = self.side_length(p1, p2)
            b = self.side_length(p2, p3)
            c = self.side_length(p1, p3)
            if a >= b + c or b >= a + c or c >= a + b:  # проверка валидности треугольника
                continue
            p = (a + b + c) / 2
            area = sqrt(p * (p - a) * (p - b) * (p - c))  # формула Герона
            if area > max_area:
                max_area = area
        return max_area
