def isValidSudoku(board):
    # Use sets to track numbers seen in rows, columns, and sub-boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sub_boxes = [set() for _ in range(9)]  # 3x3 sub-boxes
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                # Calculate sub-box index
                box_index = (i // 3) * 3 + j // 3
                
                # Check if the number already exists in the row, column, or sub-box
                if num in rows[i] or num in cols[j] or num in sub_boxes[box_index]:
                    return False
                
                # Add the number to the respective row, column, and sub-box
                rows[i].add(num)
                cols[j].add(num)
                sub_boxes[box_index].add(num)
    
    return True

# Test case 1
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Test case 2
board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Print results
print(isValidSudoku(board1))  # Expected output: True
print(isValidSudoku(board2))  # Expected output: False
