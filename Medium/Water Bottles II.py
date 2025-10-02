class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            drunk += 1
            empty = empty - numExchange + 1
            numExchange += 1
        return drunk
