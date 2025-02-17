class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        for i in range(1, len(tiles) + 1):
            sequences |= set(itertools.permutations(tiles, i))
        return len(sequences)
