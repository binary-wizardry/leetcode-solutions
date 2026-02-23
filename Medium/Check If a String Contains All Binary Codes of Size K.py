class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        flags = {f'{i:b}'.rjust(k, '0'): False for i in range(2 ** k)}
        for i in range(len(s) - k + 1):
            chunk = s[i: i + k]
            flags[chunk] = True
        return all(flags.values())
