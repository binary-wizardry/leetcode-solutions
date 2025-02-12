from string import ascii_lowercase as alphabet

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        mask = [0] * length
        for start, end, forward in shifts:
            if forward:
                mask[start] += 1
                if end + 1 < length:
                    mask[end + 1] -= 1
            else:
                mask[start] -= 1
                if end + 1 < length:
                    mask[end + 1] += 1
        
        shift = 0
        result = []
        for char, increment in zip(s, mask):
            shift += increment
            result.append(alphabet[(alphabet.index(char) + shift) % 26])
        return ''.join(result)
