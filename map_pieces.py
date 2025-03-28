import string
import numpy as np

def map_pieces_to_squares(piece_positions, squares):
    """
    Maps detected pieces to the closest chessboard square.
    """
    ranks = list(range(8, 0, -1))  
    files = list(string.ascii_lowercase[:8])

    board_dict = {}

    for x, y, piece in piece_positions:
        closest_square = None
        min_dist = float("inf")

        for idx, ((x1, y1), (x2, y2)) in enumerate(squares):
            square_center = ((x1 + x2) // 2, (y1 + y2) // 2)
            dist = np.sqrt((x - square_center[0]) ** 2 + (y - square_center[1]) ** 2)

            if dist < min_dist:
                min_dist = dist
                closest_square = idx

        if closest_square is not None:
            row = closest_square // 8
            col = closest_square % 8
            square_name = f"{files[col]}{ranks[row]}"
            board_dict[square_name] = piece

    return board_dict
