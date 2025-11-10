"""
Quick validation test for the Sudoku solver
"""

from sudoku_solver import SudokuSolver


def test_basic_solve():
    """Test that solver can find a valid solution"""
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

    solver = SudokuSolver(puzzle)
    result = solver.solve()

    print("Test 1: Basic solve")
    print(f"  Result: {'PASS' if result else 'FAIL'}")

    if result:
        # Verify solution is complete (no zeros)
        has_zeros = any(0 in row for row in solver.board)
        print(f"  Complete solution: {'PASS' if not has_zeros else 'FAIL'}")

        # Verify all rows have 1-9
        rows_valid = all(sorted(row) == list(range(1, 10)) for row in solver.board)
        print(f"  Valid rows: {'PASS' if rows_valid else 'FAIL'}")

        # Verify all columns have 1-9
        cols_valid = all(
            sorted([solver.board[row][col] for row in range(9)]) == list(range(1, 10))
            for col in range(9)
        )
        print(f"  Valid columns: {'PASS' if cols_valid else 'FAIL'}")

        print("\nSolution:")
        solver.print_board()

    return result


def test_find_all_solutions():
    """Test finding all solutions for a puzzle with unique solution"""
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

    solver = SudokuSolver(puzzle)
    solutions = solver.find_all_solutions()

    print("\n\nTest 2: Find all solutions")
    print(f"  Solutions found: {len(solutions)}")
    print(f"  Result: {'PASS' if len(solutions) == 1 else 'FAIL (expected 1 solution)'}")

    return len(solutions) == 1


def test_invalid_puzzle():
    """Test with an unsolvable puzzle"""
    # This puzzle is invalid (two 5s in first row)
    puzzle = [
        [5, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    solver = SudokuSolver(puzzle)
    result = solver.solve()

    print("\n\nTest 3: Invalid puzzle (should not solve)")
    print(f"  Result: {'PASS' if not result else 'FAIL (should not find solution)'}")

    return not result


if __name__ == "__main__":
    print("=" * 60)
    print("SUDOKU SOLVER VALIDATION TESTS")
    print("=" * 60)
    print()

    test1 = test_basic_solve()
    test2 = test_find_all_solutions()
    test3 = test_invalid_puzzle()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Test 1 (Basic solve): {'PASS' if test1 else 'FAIL'}")
    print(f"Test 2 (Find all solutions): {'PASS' if test2 else 'FAIL'}")
    print(f"Test 3 (Invalid puzzle): {'PASS' if test3 else 'FAIL'}")
    print()

    all_pass = test1 and test2 and test3
    print(f"Overall: {'ALL TESTS PASSED ✓' if all_pass else 'SOME TESTS FAILED ✗'}")
