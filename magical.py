import numpy as np

def generate_magic_square_odd(n):
    """
    Generates an n x n magic square using the Siamese method.
    n must be an odd integer.
    """
    if n % 2 == 0:
        raise ValueError("n must be an odd integer for the Siamese method.")

    magic_square = np.zeros((n, n), dtype=int)

    # Starting position for 1: middle of the top row
    i, j = 0, n // 2

    for num in range(1, n**2 + 1):
        # Place the current number in the grid
        magic_square[i, j] = num

        # Calculate the next position (up one, right one)
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # If the new cell is already filled, move vertically down one space from the current position
        if magic_square[new_i, new_j]:
            i = (i + 1) % n
            # j remains the same
        else:
            # Otherwise, move to the new position
            i, j = new_i, new_j

    return magic_square
