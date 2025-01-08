import numpy as np

def print_grid(grid):
    """Prints the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Checks if placing a number is valid."""
    # Check the row
    if num in grid[row]:
        return False
    # Check the column
    if num in grid[:, col]:
        return False
    # Check the 3x3 subgrid
    subgrid_row, subgrid_col = row // 3, col // 3
    if num in grid[subgrid_row*3:(subgrid_row+1)*3, subgrid_col*3:(subgrid_col+1)*3]:
        return False
    return True

def solve_sudoku(grid):
    """Solves Sudoku using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row, col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row, col] = 0  # Backtrack
                return False
    return True

if __name__ == "__main__":
    # Example Sudoku grid (0 represents an empty cell)
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

    print("Original Sudoku Grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists!")
