# Sudoku Grid
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
# Row Check
def possible (row, col, num):
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False
    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False
    # Check the 3x3 box
    box_row_ = (row//3)*3
    box_col_ = (col//3)*3
    for i in range (3):
        for j in range (3):
            if grid[box_row_ + i][box_col_ + j] == num:
                return False
    return True

# Backtracking Solver
def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if possible(row, col, num):
                        grid[row][col] = num
                        if solve():
                            return True
                        grid[row][col] = 0
                return False
    return True

for row in grid: # Printing the grid
    print(row)
    
