class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equal = {char: {char} for char in ascii_lowercase}
        for a, b in zip(s1, s2):
            equal[a].add(b)
            for char in equal[a]:
                equal[char] |= equal[a]
            equal[b].add(a)
            for char in equal[b]:
                equal[char] |= equal[b]

        for k, v in equal.items():
            equal[k] = min(v)
        
        return ''.join(equal[char] for char in baseStr)
