class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        obstacles = set((x, y) for x, y in obstacles)
        orient = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        dx, dy = orient[0]
        distance = 0

        for command in commands:
            if command == -1:
                orient.rotate(-1)
                dx, dy = orient[0]
            elif command == -2:
                orient.rotate(1)
                dx, dy = orient[0]
            else:
                while command:
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                    distance = max(distance, x * x + y * y)
                    command -= 1
        
        return distance
