# NOTE:     This kata appeared on my codewars dashboard. I already know how to
#           do it in C (see "sudokubacktrack.c"), I wanted to do it in Python


def isPossible(puzzle, row, col):
    currVal = puzzle[row][col]
    # check row
    for c in range(9):
        if puzzle[row][c] == currVal and c != col:
            return False
    # check col
    for r in range(9):
        if puzzle[r][col] == currVal and r != row:
            return False

    # check 3x3 block where currVal is in
    rBlock = 3 * (row//3)
    cBlock = 3 * (col//3)
    for r in range(rBlock, rBlock+3):
        for c in range(cBlock, cBlock+3):
            if r != row and c != col and puzzle[r][c] == currVal:
                return False
    # else
    return True


def bruteforce(puzzle, row, col):
    # if we finished (last recursive call), return the puzzle resolved
    if row == 9:
        """
        print("Found solution:")
        for row in puzzle:
            print(row)
        print()
        """
        return puzzle

    # set next col and row
    nextRow = row
    nextCol = col + 1
    if nextCol == 9:  # if col exceed, next row
        nextRow += 1
        nextCol = 0

    # IF: value not set, DO: try every number 1->9, each go next recursive call
    # ELSE DO: don't change the value, go to next recursive call
    if puzzle[row][col] == 0:
        for k in range(1, 10):
            puzzle[row][col] = k
            if isPossible(puzzle, row, col):
                if bruteforce(puzzle, nextRow, nextCol):
                    return puzzle
            puzzle[row][col] = 0
    else:
        if bruteforce(puzzle, nextRow, nextCol):
            return puzzle


def sudoku(puzzle):
    # check if puzzle is 9x9
    if len(puzzle) != 9:
        return False
    for row in puzzle:
        if len(row) != 9:
            return False
    # call the resolver (recursive backtracking algorithm)
    return bruteforce(puzzle, 0, 0)


"""
# MAIN_______________________
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print("resolving...")
resolvedPuzzle = sudoku(puzzle)
for row in resolvedPuzzle:
    print(row)
"""
