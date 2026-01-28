# ================================
# GUI / UX SECTION (aligned with Section 1)
# ================================

root = tk.Tk()
root.title("Sudoku – GUI")
root.geometry("500x650")

cells = [[None for _ in range(9)] for _ in range(9)]
selected = None
dark_mode = False

LIGHT_BG = "#ffffff"
DARK_BG = "#1e1e1e"
LIGHT_CELL = "#f0f0f0"
DARK_CELL = "#333333"
SELECT_COLOR = "#4CAF50"

# -----------------
# Frames
# -----------------
frame = tk.Frame(root)
frame.pack(pady=15)

num_frame = tk.Frame(root)
num_frame.pack()

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# -----------------
# Functions
# -----------------
def apply_theme():
    bg = DARK_BG if dark_mode else LIGHT_BG
    cell = DARK_CELL if dark_mode else LIGHT_CELL
    root.configure(bg=bg)
    frame.configure(bg=bg)
    num_frame.configure(bg=bg)
    control_frame.configure(bg=bg)

    for i in range(9):
        for j in range(9):
            if original[i][j] != 0:
                cells[i][j].config(bg="#777777")
            else:
                cells[i][j].config(bg=cell)
            cells[i][j].config(relief="flat", bd=2)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def highlight(r,c):
    for i in range(9):
        for j in range(9):
            if original[i][j] != 0:
                continue
            cells[i][j].config(relief="flat")
    cells[r][c].config(relief="solid", bd=3)

def select_cell(r,c):
    global selected
    selected = (r,c)
    highlight(r,c)

def refresh_grid():
    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            cells[i][j].config(text=str(val) if val != 0 else "")
    apply_theme()

def place_number(n):
    global selected
    if not selected:
        return
    r,c = selected
    if original[r][c] != 0:
        return
    if possible(r,c,n):
        grid[r][c] = n
        refresh_grid()
    else:
        messagebox.showerror("Sudoku","Invalid Move")

def clear_cell():
    global selected
    if not selected:
        return
    r,c = selected
    if original[r][c] != 0:
        return
    grid[r][c] = 0
    refresh_grid()

def reset_board():
    for i in range(9):
        for j in range(9):
            grid[i][j] = original[i][j]
    refresh_grid()

def check_solution():
    if is_complete_and_correct():
        messagebox.showinfo("Sudoku","🎉 You solved it!")
    else:
        messagebox.showerror("Sudoku","❌ Not solved yet")

# -----------------
# Draw Sudoku Grid
# -----------------
for i in range(9):
    for j in range(9):
        val = grid[i][j]
        btn = tk.Button(
            frame,
            text=str(val) if val != 0 else "",
            width=4,
            height=2,
            font=("Arial",18),
            command=lambda r=i,c=j: select_cell(r,c)
        )
        btn.grid(row=i,column=j,padx=2,pady=2)
        cells[i][j] = btn

# -----------------
# Number Buttons
# -----------------
for i in range(1,10):
    tk.Button(num_frame,text=str(i),width=4,font=("Arial",14),
              command=lambda n=i: place_number(n)).grid(row=0,column=i-1,padx=5,pady=10)

# -----------------
# Control Buttons
# -----------------
tk.Button(control_frame,text="Clear",command=clear_cell).grid(row=0,column=0,padx=5)
tk.Button(control_frame,text="Reset",command=reset_board).grid(row=0,column=1,padx=5)
tk.Button(control_frame,text="Check",command=check_solution).grid(row=0,column=2,padx=5)
tk.Button(control_frame,text="Dark / Light",command=toggle_theme).grid(row=0,column=3,padx=5)

# -----------------
# Initialize Theme
# -----------------
apply_theme()
root.mainloop()