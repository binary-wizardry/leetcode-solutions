class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ''
        
        cols = len(encodedText) // rows
        matrix = [list(row) for row in batched(encodedText, cols)]
        
        result = []
        for diag in range(cols):
            inc = 0
            while diag + inc < cols and inc < rows:
                result.append(matrix[inc][diag + inc])
                inc += 1
        
        return ''.join(result).rstrip()
        
