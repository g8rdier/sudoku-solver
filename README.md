# Sudoku Solver

Ein Python-Programm zum Lösen von Sudoku-Rätseln mit Backtracking-Algorithmus.

## Funktionen

- Löst Sudoku-Rätsel mit Backtracking-Algorithmus
- Findet alle möglichen Lösungen und zählt diese
- Validiert Lösungen nach Sudoku-Regeln (Zeile, Spalte, 3x3 Box)

## Anforderungen

- Python 3.6 oder höher

## Verwendung

```python
from sudoku_solver import SudokuSolver

# Sudoku-Rätsel als 9x9 Array (0 = leeres Feld)
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

# Solver initialisieren
solver = SudokuSolver(puzzle)

# Erste Lösung finden
if solver.solve():
    print("Lösung gefunden:")
    solver.print_board()

# Alle Lösungen finden
solver.reset()
all_solutions = solver.find_all_solutions()
print(f"Anzahl der Lösungen: {len(all_solutions)}")
```

## Beispiel ausführen

```bash
python sudoku_solver.py
```

## Algorithmus

Das Programm verwendet den **Backtracking-Algorithmus**:

1. Finde eine leere Zelle (0)
2. Probiere Zahlen von 1-9 aus
3. Prüfe ob die Zahl gültig ist (Zeile, Spalte, 3x3 Box)
4. Wenn gültig, setze die Zahl und gehe rekursiv weiter
5. Wenn keine Lösung gefunden wird, gehe zurück (Backtrack) und probiere die nächste Zahl

## Klassen und Methoden

### `SudokuSolver`

- `__init__(board)`: Initialisiert den Solver mit einem 9x9 Board
- `solve()`: Findet die erste Lösung
- `find_all_solutions()`: Findet alle möglichen Lösungen
- `count_solutions()`: Zählt die Anzahl der Lösungen
- `print_board(board)`: Gibt das Board formatiert aus
- `is_valid(row, col, num)`: Prüft ob eine Zahl an der Position gültig ist
- `reset()`: Setzt das Board auf den Ausgangszustand zurück

## Beispiel-Output

```
==================================================
SUDOKU SOLVER
==================================================

Original Puzzle:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

Solution found:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

Total number of solutions: 1
```

## Lizenz

MIT License
