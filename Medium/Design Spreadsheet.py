class Spreadsheet:

    def __init__(self, rows: int):
        self.excel = {char: [0] * rows for char in ascii_uppercase}
        # actually here we just can use map like {'A1': int}
        # it would be easier and faster

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.cell_indexes(cell)
        self.excel[col][row] = value

    def resetCell(self, cell: str) -> None:
        col, row = self.cell_indexes(cell)
        self.excel[col][row] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        a = int(a) if a.isdigit() else self.getCell(a)
        b = int(b) if b.isdigit() else self.getCell(b)
        return a + b

    def cell_indexes(self, cell: str) -> (str, int):
        return cell[:1], int(cell[1:]) - 1
    
    def getCell(self, cell: str) -> int:
        col, row = self.cell_indexes(cell)
        return self.excel[col][row]

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
