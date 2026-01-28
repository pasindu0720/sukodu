# =================================
# Sudoku Game (CLI + GUI-Ready)
# =================================

# -------------------------------
# Sudoku Grid (0 = empty)
# -------------------------------
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

# Lock original cells
original = [row[:] for row in grid]

# -------------------------------
# Check if move is valid
# -------------------------------
def possible(row, col, num):
    # Row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False

    return True

# -------------------------------
# Sudoku Solver (Backtracking)
# -------------------------------
def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if possible(row, col, num):
                        grid[row][col] = num
                        if solve():
                            return True
                        grid[row][col] = 0
                return False
    return True

# -------------------------------
# Check if user's solution is correct
# -------------------------------
def is_complete_and_correct():
    # Check for empty cells
    for row in grid:
        if 0 in row:
            return False

    # Create a copy and solve it
    solution = [row[:] for row in grid]
    
    def solve_copy(g):
        for r in range(9):
            for c in range(9):
                if g[r][c] == 0:
                    for n in range(1, 10):
                        if possible_copy(g, r, c, n):
                            g[r][c] = n
                            if solve_copy(g):
                                return True
                            g[r][c] = 0
                    return False
        return True

    def possible_copy(g, row, col, num):
        for x in range(9):
            if g[row][x] == num or g[x][col] == num:
                return False

        br, bc = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if g[br + i][bc + j] == num:
                    return False
        return True

    solve_copy(solution)

    return grid == solution

# -------------------------------
# Print Board
# -------------------------------
def print_grid():
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

# -------------------------------
# Game Controls
# -------------------------------
def game_controls():
    while True:
        print("\nSudoku Board:")
        print_grid()

        print("\nControls:")
        print("p row col num  → place number")
        print("d row col      → delete cell (DEL)")
        print("s              → solve")
        print("q              → quit")

        cmd = input("\nEnter command: ").lower().split()

        if not cmd:
            continue

        # Quit
        if cmd[0] == "q":
            print("Game exited.")
            break

        # Solve
        if cmd[0] == "s":
            if is_complete_and_correct():
                print("\n🎉 Congratulations, you have done it!")
            else:
                print("\n❌ Something's wrong, try again!")
            print_grid()
            break

        try:
            # Place number
            if cmd[0] == "p":
                if len(cmd) != 4:
                    print("❌ Invalid format. Example: p 1 3 4")
                    continue
                _, row, col, num = cmd
                row, col, num = int(row)-1, int(col)-1, int(num)

                if original[row][col] != 0:
                    print("❌ Locked cell")
                    continue

                if 1 <= num <= 9 and possible(row, col, num):
                    grid[row][col] = num
                    print(f"✅ Placed {num} at ({row+1}, {col+1})")
                else:
                    print("❌ Invalid move")

            # Delete number
            elif cmd[0] == "d":
                if len(cmd) != 3:
                    print("❌ Invalid format. Example: d 1 3")
                    continue
                _, row, col = cmd
                row, col = int(row)-1, int(col)-1

                if original[row][col] != 0:
                    print("❌ Locked cell")
                    continue

                grid[row][col] = 0
                print(f"🗑️ Cleared cell ({row+1}, {col+1})")

            else:
                print("❌ Unknown command")

        except Exception as e:
            print("❌ Invalid input format")

# -------------------------------
# Start Game
# -------------------------------
game_controls()
