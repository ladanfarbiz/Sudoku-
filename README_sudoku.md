Sudoku Solver - Puzzle games XD

Overview

The Sudoku Solver is a Python-based project designed to solve Sudoku puzzles using two approaches:
	1.	Backtracking Algorithm: A recursive method to solve Sudoku puzzles efficiently.
	2.	Mixed Integer Programming (MIP): Solves the problem using PuLP, a Python library for linear programming.

The project can handle Sudoku puzzles of any valid size (commonly 9x9) and allows custom puzzle input. It demonstrates the application of algorithmic thinking and optimization techniques to solve constraint satisfaction problems.

Features
	•	Input: Accepts partially completed Sudoku puzzles.
	•	Output: Fully solved puzzles or a message indicating no solution exists.
	•	Algorithms:
	•	Backtracking: Classic recursive method for solving Sudoku.
	•	MIP: Constraint programming approach using PuLP.
	•	Optional: Visualize the puzzle grid before and after solving.

Technologies Used
	•	Programming Language: Python
	•	Libraries:
	•	NumPy: For efficient array manipulation.
	•	PuLP: For Mixed Integer Programming (optional approach).
	•	Matplotlib: For visualizing Sudoku grids (optional).
	•	IDE/Environment: Works in any Python 3.x environment.

File Structure

/SudokuSolver
├── sudoku_solver.py       # Backtracking-based Sudoku solver
├── sudoku_mip_solver.py   # MIP-based Sudoku solver using PuLP
├── sudoku_input.txt       # Example Sudoku puzzles
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # Project license

How to Run

Prerequisites
	1.	Install Python 3.x from python.org.
	2.	Install the required Python libraries:

pip install numpy pulp matplotlib



Backtracking Solver

Run the sudoku_solver.py script:

python sudoku_solver.py

MIP Solver

Run the sudoku_mip_solver.py script:

python sudoku_mip_solver.py

Custom Puzzle Input

Modify the grid in either script:

sudoku_grid = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

Example Output

Input Puzzle:

5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Solved Puzzle:

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9



Contact

Developed by Ladan Farbiz
Email: ladanfarbiz@yahoo.com
GitHub: [Your GitHub Profile Link]

Acknowledgments
	•	Inspiration from algorithmic problem-solving challenges.
	•	PuLP for making constraint programming accessible.
	•	NumPy and Matplotlib for enhancing development and visualization.
