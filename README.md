# 🎮 Sudoku Game

A feature-rich Sudoku game built with Python and Tkinter, featuring a beautiful GUI, timer, hint system, save/load functionality, and dark mode.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

---

## ✨ Features

### Core Gameplay
- ✅ **Interactive 9x9 Sudoku Grid** - Click to select cells
- ✅ **Smart Validation** - Real-time checking of valid moves
- ✅ **Backtracking Solver** - Automatic puzzle solving algorithm
- ✅ **Original Cell Locking** - Initial puzzle cells cannot be modified
- ✅ **Solution Verification** - Check if your solution is correct

### User Interface
- 🎨 **Light/Dark Mode** - Toggle between themes
- 🖱️ **Mouse & Keyboard Input** - Full control options
- 📱 **Responsive Design** - Clean and intuitive interface
- 🔢 **Number Pad** - Quick number entry buttons
- 🎯 **Cell Highlighting** - Visual feedback for selected cell

### Advanced Features
- ⏱️ **Timer** - Track how long you've been playing
- 💡 **Hint System** - Get hints for difficult cells
- ❌ **Mistake Counter** - Track your errors
- 💾 **Save/Load Game** - Continue your game later
- 🔄 **Reset Function** - Start over from the original puzzle

---

## 📸 Screenshots


<img width="1117" height="983" alt="image" src="https://github.com/user-attachments/assets/a22e99d4-91d2-4d3e-8cad-98918c90f248" />



## 🎮 How to Play

### Basic Controls

#### Mouse Controls:
1. **Click a cell** to select it (highlighted in color)
2. **Click number buttons** (1-9) to place a number
3. **Click "Clear"** to remove a number from selected cell

#### Keyboard Controls:
- **1-9 keys** - Place number in selected cell
- **0 or Delete/Backspace** - Clear selected cell
- **Mouse click** - Select different cell

### Game Buttons

| Button | Function |
|--------|----------|
| **Numbers 1-9** | Enter number in selected cell |
| **Clear** | Remove number from selected cell |
| **Reset** | Reset puzzle to original state |
| **Check** | Verify if solution is correct |
| **Dark/Light** | Toggle between color themes |
| **Hint** | Get a hint for an empty cell |
| **Save** | Save current game progress |
| **Load** | Load previously saved game |

### Game Rules

1. **Fill the 9×9 grid** so that each column, each row, and each of the nine 3×3 boxes contains the digits 1-9
2. **No repetition** - Each number can appear only once in each row, column, and 3×3 box
3. **Pre-filled cells** (shown in darker color) cannot be modified
4. **Invalid moves** will show an error message

### Tips & Strategies

- 🎯 **Start with easiest** - Fill in cells where only one number is possible
- 🔍 **Process of elimination** - Look at rows, columns, and boxes together
- 💡 **Use hints sparingly** - Try to solve as much as possible yourself
- ⏱️ **No time limit** - Take your time and think strategically
- 💾 **Save your progress** - Come back to difficult puzzles later



### File Descriptions

#### **main.py**
- Entry point of the application
- Initializes engine, addons, and GUI
- Connects all components together
- Starts the game loop

#### **engine.py**
- `SudokuEngine` class containing:
  - Grid management
  - Move validation (`possible()` method)
  - Backtracking solver algorithm
  - Solution verification
  - Board reset functionality

#### **gui.py**
- `SudokuGUI` class containing:
  - Tkinter-based user interface
  - Cell rendering and interaction
  - Theme management (light/dark mode)
  - Button controls
  - Event handling (mouse + keyboard)

#### **addons.py**
- `AddonManager` class containing:
  - Timer functionality
  - Mistake counter
  - Hint system
  - Save/Load game state (JSON format)

---

## 🔧 Technical Details

### Algorithm: Backtracking

The solver uses a **recursive backtracking algorithm**:

1. Find an empty cell (value = 0)
2. Try numbers 1-9 in that cell
3. Check if the number is valid (row, column, 3×3 box rules)
4. If valid, place number and recursively solve next cell
5. If stuck, backtrack and try different number
6. Repeat until solution found or all possibilities exhausted

**Time Complexity:** O(9^(n*n)) worst case, where n=9
**Space Complexity:** O(n*n) for the grid storage

### Data Structures

- **Grid:** 2D list (9x9) - `[[int]]`
- **Original:** Copy of initial puzzle - `[[int]]`
- **Cells:** Dictionary mapping (row, col) to tkinter widgets

### Validation Logic

A number is valid at position (row, col) if:
```python
✓ Not present in the same row
✓ Not present in the same column
✓ Not present in the same 3×3 box
```

---

## 👨‍💻 Development

### Requirements
- Python 3.7+
- tkinter (standard library)
- json (standard library)
- time (standard library)

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sudoku-game.git
   cd sudoku-game
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable names
- Comment complex logic
- Keep functions focused and modular

### Testing Checklist

Before committing changes, verify:
- [ ] Application starts without errors
- [ ] All buttons function correctly
- [ ] Cell selection works (mouse + keyboard)
- [ ] Number input validation works
- [ ] Reset button restores original puzzle
- [ ] Check button correctly verifies solution
- [ ] Theme toggle works
- [ ] Timer counts correctly
- [ ] Save/Load functionality works
- [ ] Hint system provides valid hints
- [ ] Original cells cannot be modified

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### **Issue 1: ModuleNotFoundError: No module named 'tkinter'**

**Solution (Windows):**
Reinstall Python and ensure "tcl/tk and IDLE" is checked during installation.

---

#### **Issue 2: Application doesn't start / No window appears**

**Check:**
1. Ensure you're running `main.py`, not individual modules
2. Verify Python version: `python --version` (must be 3.7+)
3. Check for error messages in terminal

**Fix:**
```bash
python main.py 2>&1 | tee error.log
```
This will save errors to `error.log` for debugging.

---

#### **Issue 3: "NameError: name 'grid' is not defined"**

**Cause:** Files are not properly connected

**Solution:**
1. Ensure `main.py` exists and imports all modules
2. Run `python main.py`, not `python gui.py`
3. Check that engine.py defines `self.grid` in the class

---

#### **Issue 4: Numbers appear but validation doesn't work**

**Check:**
- Engine's `possible()` method is being called
- Grid is being updated correctly
- No conflicting global variables

**Debug:**
Add print statements in `possible()` method to verify it's being called.

---

#### **Issue 5: Save/Load doesn't work**

**Possible causes:**
1. No write permissions in directory
2. JSON file corrupted

**Solution:**
```bash
# Check if file is created
ls -la sudoku_save.json

# Delete corrupted file
rm sudoku_save.json

# Try saving again
```

---

#### **Issue 6: Dark mode doesn't apply properly**

**Solution:**
Click the "Dark/Light" button twice to refresh the theme properly.


---


### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add feature X"`
6. Push to your fork: `git push origin feature-name`
7. Submit a pull request

### Code Contribution Guidelines
- Follow existing code style
- Add comments for complex logic
- Update README if needed
- Test your changes before submitting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License
Copyright (c) 2026 Maths Group C 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

---

## 👏 Credits

### Developer
 **Minaga Sanviru** - Leader / Engine.
 **Pasidu Eshan** - Gui 
 **Sachin ** - Gui 
 **Riveen Perera ** - Controls 
 ** Chalaka Fernando ** - Controls 
- 

### Technologies Used
- **Python 3** - Programming language
- **Tkinter** - GUI framework
- **JSON** - Save/load functionality

### Inspiration
This project was created as part of a Mathematics for Computing course, combining:
- Algorithm design (backtracking)
- Data structures (2D arrays, recursion)
- Software engineering (modular design)
- User interface design

### Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Sudoku Rules](https://en.wikipedia.org/wiki/Sudoku)
- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)

---

## 📞 Contact & Support

### Questions or Issues?
- **GitHub Issues:** [Create an issue](https://github.com/pasindu0720/sudoku-game/issues)
- **Discussions:** [Join discussions](https://github.com/pasindu0720/sudoku-game/discussions)

### Social Media
- **Twitter:** @yourusername
- **LinkedIn:** linkedin.com/in/yourusername

---

## 📊 Project Stats

- **Language:** Python
- **Lines of Code:** ~500
- **Files:** 4 main modules
- **Dependencies:** Standard library only
- **Platform:** Cross-platform (Windows)

---

## 🎓 Educational Value

This project demonstrates:
- **Object-Oriented Programming** - Classes and encapsulation
- **Algorithm Design** - Backtracking recursion
- **GUI Development** - Event-driven programming
- **File I/O** - JSON serialization
- **Software Architecture** - Modular design pattern

Great for:
- Learning Python
- Understanding algorithms
- GUI programming practice
- Portfolio project

---

## ⭐ Star This Project

If you found this project helpful or interesting, please consider giving it a star! ⭐

It helps others discover the project and motivates continued development.

---

## 📝 Changelog

### Version 1.0.0 (Current)
- ✅ Initial release
- ✅ Core Sudoku gameplay
- ✅ GUI with light/dark themes
- ✅ Timer and mistake counter
- ✅ Hint system
- ✅ Save/load functionality

### Upcoming in Version 1.1.0
- 🔜 Puzzle generator
- 🔜 Difficulty levels
- 🔜 Undo/redo feature

---

## 🙏 Acknowledgments

Special thanks to:
- The Python community for excellent documentation
- Contributors and testers
- Mathematics for Computing course instructors
- All Sudoku enthusiasts who inspired this project


**Made with ❤️ and Python**

[⬆ Back to Top](#-sudoku-game)

</div>
