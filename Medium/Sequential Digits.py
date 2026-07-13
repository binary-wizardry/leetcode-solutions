class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential = []
        for places in range(2, 10):
            for ini in range(1, 10 - places + 1):
                number = []
                for digit in range(ini, ini + places):
                    number.append(digit)
                sequential.append(int(''.join(map(str, number))))
        return list(dropwhile(lambda x: x < low, takewhile(lambda x: x <= high, sequential)))
