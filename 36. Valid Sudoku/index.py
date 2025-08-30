class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue  # skip empty cells

                # find which 3x3 box (index 0-8)
                box_index = (r // 3) * 3 + (c // 3)

                # if duplicate found in row, column, or box → invalid
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False

                # otherwise, record the value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True
