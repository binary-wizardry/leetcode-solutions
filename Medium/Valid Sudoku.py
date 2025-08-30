class Solution:
    def check(self, numbers: list[int]) -> bool:
        hashmap = set()
        for num in numbers:
            if num in hashmap:
                return False
            else:
                hashmap.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [int(num) for num in board[i] if num.isdigit()]
            col = [int(board[j][i]) for j in range(9) if board[j][i].isdigit()]
            if not self.check(row) or not self.check(col):
                return False
        for i in range(3):
            for j in range(3):
                square = [int(board[r][c]) for r in range(i*3, i*3+3) for c in range(j*3, j*3+3) if board[r][c].isdigit()]
                if not self.check(square):
                    return False
        return True
