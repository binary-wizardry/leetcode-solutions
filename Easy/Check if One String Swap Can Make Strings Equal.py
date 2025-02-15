class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        nonequal = []
        for a, b in zip(s1, s2):
            if a != b:
                nonequal += [a, b]
            if len(nonequal) > 4:
                return False
        return len(nonequal) == 0 or len(nonequal)  == 4 and (nonequal[0], nonequal[1]) == (nonequal[3], nonequal[2])
