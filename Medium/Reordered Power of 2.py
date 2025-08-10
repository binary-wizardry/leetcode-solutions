class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(int(i) for i in str(n))
        power = 1
        length = len(str(n))
        while len(str(power)) < length:
            power <<= 1
        
        while len(str(power)) == length:
            test = Counter(int(i) for i in str(power))
            if test == digits:
                return True 
            power <<= 1
        return False
