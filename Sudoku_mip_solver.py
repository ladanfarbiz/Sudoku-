from pulp import LpProblem, LpVariable, lpSum, LpBinary, LpStatus, value
import numpy as np

def solve_sudoku_mip(grid):
    """Solves Sudoku using Mixed Integer Programming."""
    prob = LpProblem("SudokuSolver")
    vars = LpVariable.dicts("cell", (range(9), range(9), range(1, 10)), 0, 1, LpBinary)

    # Constraints: Fill already provided numbers
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                prob += vars[row][col][grid[row][col]] == 1

    # Constraints: Only one number per cell
    for row in range(9):
        for col in range(9):
            prob += lpSum([vars[row][col][num] for num in range(1, 10)]) == 1

    # Constraints: Unique numbers in each row, column, and 3x3 subgrid
    for num in range(1, 10):
        for row in range(9):
            prob += lpSum([vars[row][col][num] for col in range(9)]) == 1
        for col in range(9):
            prob += lpSum([vars[row][col][num] for row in range(9)]) == 1
        for sub_row in range(3):
            for sub_col in range(3):
                prob += lpSum([
                    vars[row][col][num]
                    for row in range(sub_row*3, (sub_row+1)*3)
                    for col in range(sub_col*3, (sub_col+1)*3)
                ]) == 1

    # Solve the problem
    prob.solve()
    if LpStatus[prob.status] == "Optimal":
        solved_grid = np.zeros((9, 9), dtype=int)
        for row in range(9):
            for col in range(9):
                for num in range(1, 10):
                    if value(vars[row][col][num]) == 1:
                        solved_grid[row][col] = num
        return solved_grid
    else:
        return None

if __name__ == "__main__":
    # Example grid
    grid = np.array([
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

    solved_grid = solve_sudoku_mip(grid)
    if solved_grid is not None:
        print("Solved Sudoku Grid:")
        print(solved_grid)
    else:
        print("No solution found!")
