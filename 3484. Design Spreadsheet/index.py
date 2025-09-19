from typing import Tuple

class Spreadsheet:
    def __init__(self, rows: int):
        # 26 columns ('A' to 'Z'), rows given
        self.rows = rows
        self.cols = 26
        # initialize all cells to 0
        self.grid = [[0] * self.cols for _ in range(rows)]

    def _parse_cell(self, cell: str) -> Tuple[int, int]:
        """Convert cell like 'A1' -> (row, col) in 0-indexed format."""
        col = ord(cell[0]) - ord('A')  # 'A'->0, 'B'->1, ...
        row = int(cell[1:]) - 1        # 1-indexed -> 0-indexed
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def _get_value_from_token(self, token: str) -> int:
        """Token could be a number or a cell reference."""
        if token[0].isdigit():  # number
            return int(token)
        else:  # cell reference
            row, col = self._parse_cell(token)
            return self.grid[row][col]

    def getValue(self, formula: str) -> int:
        # formula looks like "=A1+B1+10"
        formula = formula[1:]  # remove '='
        tokens = formula.split('+')
        return sum(self._get_value_from_token(t.strip()) for t in tokens)


# Example usage
if __name__ == "__main__":
    sheet = Spreadsheet(5)  # spreadsheet with 5 rows
    sheet.setCell("A1", 10)
    sheet.setCell("B1", 20)
    sheet.setCell("C1", 30)

    print("A1:", sheet.grid[0][0])
    print("B1:", sheet.grid[0][1])
    print("C1:", sheet.grid[0][2])
    print("Formula (=A1+B1+C1+50):", sheet.getValue("=A1+B1+C1+50"))
