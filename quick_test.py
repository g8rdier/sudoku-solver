"""Quick test to validate solver works"""

from sudoku_solver import SudokuSolver

# Simple test puzzle
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Puzzle:")
solver = SudokuSolver(puzzle)
solver.print_board()

print("\nSolving...")
if solver.solve():
    print("\nSolution found:")
    solver.print_board()

    # Validate
    has_zeros = any(0 in row for row in solver.board)
    rows_valid = all(sorted(row) == list(range(1, 10)) for row in solver.board)

    print(f"\nValidation:")
    print(f"  Complete (no zeros): {not has_zeros}")
    print(f"  Valid rows (1-9): {rows_valid}")
    print(f"\nResult: {'SUCCESS' if not has_zeros and rows_valid else 'FAILED'}")
else:
    print("\nNo solution found - FAILED")
