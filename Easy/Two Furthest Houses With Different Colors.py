class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        dist = 0

        for i, color in enumerate(colors):
            if color != colors[0]:
                dist = i
            
        for i, color in enumerate(reversed(colors)):
            if color != colors[n - 1]:
                dist = max(dist, i)
        
        return dist
