class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors ={}
        balls ={}
        result = []
        for ball, color in queries:
            if ball in balls:
                previous_color = balls[ball]
                colors[previous_color] -= 1
                if not colors[previous_color]:
                    del colors[previous_color]
            balls[ball] = color
            colors[color] = colors.get(color, 0) + 1
            result.append(len(colors))
        return result
