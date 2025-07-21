# Maze Solver

This project generates and solves a grid-based maze using Tkinter in Python. It visualizes both the maze generation and the solution process in a GUI window.

## Features

- Maze generation with customizable number of rows and columns
- Visualization using Tkinter GUI
- Automatic maze solving using recursive backtracking (DFS)
- Step-by-step solution display

## Requirements

- Python 3.12 or newer
- Tkinter (included with standard Python installations)

## Getting Started

1. **Clone the repository**
2. **Run the main program:**
   ```sh
   python main.py
   ```
   You can adjust the maze size by editing `num_rows` and `num_cols` in [main.py](main.py).

## Running Tests

Unit tests are provided in [tests.py](tests.py). Run them with:
```sh
python tests.py
```

## Project Structure

- `main.py` — Entry point, sets up the window and maze
- `maze.py` — Maze generation and solving logic
- `cell.py`, `line.py`, `point.py` — Supporting classes for maze structure and drawing
- `window.py` — Tkinter window and drawing utilities
- `tests.py` — Unit tests

## License

This project is for educational purposes as part of a Boot.dev learning module.