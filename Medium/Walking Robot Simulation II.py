class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.mod = 2 * (self.width - 1) + 2 * (self.height - 1)
        self.track = deque(
            [[x, 0] for x in range(width)] + 
            [[width - 1, y] for y in range(1, height)] +
            [[width - 1 - x, height - 1] for x in range(1, width)] +
            [[0, height -1 - y] for y in range(1, height - 1)])
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.track.rotate(-num % self.mod)

    def getPos(self) -> List[int]:
        return self.track[0]

    def getDir(self) -> str:
        match self.getPos():
            case [0, 0] if not self.moved:
                return 'East'
            case [0, 0] if self.moved:
                return 'South'
            case [_, 0]:
                return 'East'
            case [x, _] if x == self.width - 1:
                return 'North'
            case [_, y] if y == self.height - 1:
                return 'West'
            case [0, _]:
                return 'South'



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
