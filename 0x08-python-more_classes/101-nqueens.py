#!/usr/bin/python3
""" Task 3.
"""
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list): The chessboard represented as a 2D list.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if N < 4:
        print("N must be at least 4")
        return

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    
    def place_queen(row):
        if row == N:
            solution = []
            for i in range(N):
                solution.append("".join("Q" if board[i][j] == 1 else "." for j in range(N)))
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                place_queen(row + 1)
                board[row][col] = 0
    
    place_queen(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

