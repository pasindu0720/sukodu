# =====================================
# Add-ons & Packaging Features
# Sudoku Project – Maths for Computing
# =====================================

import time
import json
from tkinter import messagebox

# -----------------------------
# Timer Feature
# -----------------------------
start_time = time.time()

def update_timer(label, root):
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60
    label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
    root.after(1000, update_timer, label, root)

# -----------------------------
# Mistake Counter
# -----------------------------
mistakes = 0

def add_mistake(label):
    global mistakes
    mistakes += 1
    label.config(text=f"Mistakes: {mistakes}")

# -----------------------------
# Hint System
# -----------------------------
def give_hint(grid, possible, refresh_grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if possible(r, c, n):
                        grid[r][c] = n
                        refresh_grid()
                        return

# -----------------------------
# Save & Load Game
# -----------------------------
def save_game(grid, mistakes):
    data = {"grid": grid, "mistakes": mistakes}
    with open("sudoku_save.json", "w") as f:
        json.dump(data, f)
    messagebox.showinfo("Sudoku", "Game Saved")

def load_game(grid):
    global mistakes
    try:
        with open("sudoku_save.json", "r") as f:
            data = json.load(f)
        for i in range(9):
            for j in range(9):
                grid[i][j] = data["grid"][i][j]
        mistakes = data["mistakes"]
        return mistakes
    except:
        messagebox.showerror("Sudoku", "No saved game found")
        return mistakes
