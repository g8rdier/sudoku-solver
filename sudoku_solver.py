"""
Sudoku Solver
A program that solves Sudoku puzzles using backtracking algorithm.
Finds all possible solutions and counts them.
"""


class SudokuSolver:
    def __init__(self, board):
        """
        Initialize the Sudoku solver with a 9x9 board.

        Args:
            board: A 9x9 list of lists where 0 represents empty cells
                   and numbers 1-9 represent filled cells.
        """
        self.board = [row[:] for row in board]  # Create a copy
        self.original_board = [row[:] for row in board]
        self.solutions = []

    def is_valid(self, row, col, num):
        """
        Check if placing a number at the given position is valid.

        Args:
            row: Row index (0-8)
            col: Column index (0-8)
            num: Number to place (1-9)

        Returns:
            True if the placement is valid, False otherwise
        """
        # Check row
        if num in self.board[row]:
            return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def find_empty_cell(self):
        """
        Find the next empty cell in the board.

        Returns:
            Tuple (row, col) of the empty cell, or None if board is full
        """
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        """
        Solve the Sudoku puzzle and return the first solution.

        Returns:
            True if a solution is found, False otherwise
        """
        empty_cell = self.find_empty_cell()

        # If no empty cell, puzzle is solved
        if empty_cell is None:
            return True

        row, col = empty_cell

        # Try numbers 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                # Backtrack
                self.board[row][col] = 0

        return False

    def find_all_solutions(self):
        """
        Find all possible solutions to the Sudoku puzzle.

        Returns:
            List of all solutions (each solution is a 9x9 board)
        """
        self._find_all_recursive()
        return self.solutions

    def _find_all_recursive(self):
        """
        Recursive helper method to find all solutions.
        """
        empty_cell = self.find_empty_cell()

        # If no empty cell, we found a solution
        if empty_cell is None:
            # Store a copy of the current solution
            solution = [row[:] for row in self.board]
            self.solutions.append(solution)
            return

        row, col = empty_cell

        # Try numbers 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                self._find_all_recursive()
                # Backtrack
                self.board[row][col] = 0

    def count_solutions(self):
        """
        Count the number of possible solutions.

        Returns:
            Number of solutions
        """
        if not self.solutions:
            self.find_all_solutions()
        return len(self.solutions)

    def print_board(self, board=None):
        """
        Print the Sudoku board in a readable format.

        Args:
            board: Board to print (defaults to current board)
        """
        if board is None:
            board = self.board

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(board[i][j], end=" ")
            print()

    def reset(self):
        """Reset the board to its original state."""
        self.board = [row[:] for row in self.original_board]
        self.solutions = []


def main():
    """Example usage of the Sudoku solver."""

    # Example Sudoku puzzle (0 represents empty cells)
    puzzle1 = [
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

    print("=" * 50)
    print("SUDOKU SOLVER")
    print("=" * 50)
    print("\nOriginal Puzzle:")
    solver = SudokuSolver(puzzle1)
    solver.print_board()

    # Find first solution
    print("\n" + "=" * 50)
    print("Finding first solution...")
    print("=" * 50)
    solver.reset()
    if solver.solve():
        print("\nSolution found:")
        solver.print_board()
    else:
        print("\nNo solution exists!")

    # Find all solutions
    print("\n" + "=" * 50)
    print("Finding all solutions...")
    print("=" * 50)
    solver.reset()
    all_solutions = solver.find_all_solutions()
    num_solutions = len(all_solutions)

    print(f"\nTotal number of solutions: {num_solutions}")

    if num_solutions > 0:
        for idx, solution in enumerate(all_solutions, 1):
            print(f"\n--- Solution {idx} ---")
            solver.print_board(solution)

    # Example with multiple solutions (incomplete puzzle)
    print("\n" + "=" * 50)
    print("EXAMPLE WITH MULTIPLE SOLUTIONS")
    print("=" * 50)

    puzzle2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]

    print("\nPuzzle with fewer constraints:")
    solver2 = SudokuSolver(puzzle2)
    solver2.print_board()

    print("\nFinding all solutions (this may take a moment)...")
    all_solutions2 = solver2.find_all_solutions()
    print(f"\nTotal number of solutions: {len(all_solutions2)}")

    if len(all_solutions2) <= 5:
        for idx, solution in enumerate(all_solutions2, 1):
            print(f"\n--- Solution {idx} ---")
            solver2.print_board(solution)
    else:
        print("\n(Showing first 3 solutions)")
        for idx, solution in enumerate(all_solutions2[:3], 1):
            print(f"\n--- Solution {idx} ---")
            solver2.print_board(solution)


if __name__ == "__main__":
    main()
