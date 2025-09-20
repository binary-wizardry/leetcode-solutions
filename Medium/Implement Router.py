class Router:

    def __init__(self, memoryLimit: int):
        self.packets = set()
        self.destination_to_time = {}
        self.q = deque([], memoryLimit)
        self.memoryLimit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = source, destination, timestamp
        if packet in self.packets:
            return False
        if len(self.q) == self.memoryLimit:
            self.forwardPacket()
        self.packets.add(packet)
        self.destination_to_time.setdefault(destination, deque()).append(timestamp)
        self.q.append(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.popleft()
        self.packets.remove(packet)
        destination = packet[1]
        self.destination_to_time[destination].popleft()
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        times = self.destination_to_time.get(destination, [])

        a, b = 0, len(times) - 1
        while a <= b:
            index = (a + b) // 2
            if times[index] < startTime:
                a = index + 1
            else:
                b = index - 1
        start = a
        
        a, b = 0, len(times) - 1
        while a <= b:
            index = (a + b) // 2
            if times[index] > endTime:
                b = index - 1
            else:
                a = index + 1
        end = b
        return end - start + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
