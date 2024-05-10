def is_safe(board, row, col, N):
    """
    Check if placing a queen at a given position is safe.

    Parameters:
    - board: 2D list representing the chessboard configuration
    - row, col: Position to check for placing the queen
    - N: Size of the chessboard (N x N)

    Returns:
    - True if placing a queen at the given position is safe, False otherwise
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    """
    Utility function to solve the N-Queens problem recursively.

    Parameters:
    - board: 2D list representing the chessboard configuration
    - row: Current row being processed
    - N: Size of the chessboard (N x N)

    Returns:
    - True if a solution is found, False otherwise
    """
    if row == N:  # Base case: If all queens are placed successfully
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):  # Check if placing a queen at (row, col) is safe
            board[row][col] = 1  # Place the queen at (row, col)
            
            if solve_n_queens_util(board, row + 1, N):  # Recur for next row
                return True
            
            board[row][col] = 0  # If placing queen at (row, col) doesn't lead to a solution, backtrack
    
    return False

def solve_n_queens(N):
    """
    Solve the N-Queens problem and print the solution.

    Parameters:
    - N: Size of the chessboard (N x N)
    """
    board = [[0] * N for _ in range(N)]  # Initialize empty chessboard
    if not solve_n_queens_util(board, 0, N):  # If no solution exists
        print("No solution exists")
        return
    
    print("Solution for {}-Queens problem:".format(N))
    for row in board:
        print(" ".join(map(str, row)))  # Print the chessboard configuration with queens placed

# Example usage:
N = 4  # Size of the chessboard
solve_n_queens(N)  # Solve the N-Queens problem and print the solution
