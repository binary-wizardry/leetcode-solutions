class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])
        result = [[''] * n for _ in range(m)]
        
        for i, row in enumerate(boxGrid):
            row = ''.join(row).split('*')
            row = '*'.join(''.join(sorted(part, reverse=True)) for part in row)
            for j, item in enumerate(row):
                result[j][~i] = item
        return result
