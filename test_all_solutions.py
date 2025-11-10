"""Test finding all solutions - uses a puzzle with known unique solution"""

from sudoku_solver import SudokuSolver
import time

# Well-formed puzzle with exactly 1 solution
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

print("Finding all solutions...")
solver = SudokuSolver(puzzle)

start = time.time()
all_solutions = solver.find_all_solutions()
end = time.time()

print(f"\nFound {len(all_solutions)} solution(s) in {end - start:.3f} seconds")

if len(all_solutions) > 0:
    print("\nSolution 1:")
    solver.print_board(all_solutions[0])

print(f"\nResult: {'SUCCESS' if len(all_solutions) == 1 else f'UNEXPECTED - found {len(all_solutions)} solutions'}")
